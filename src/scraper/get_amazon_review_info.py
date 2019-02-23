import requests
import urllib
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import base64

DEFAULT_HEADERS = {
    "Authority":
    "www.amazon.ca",
    "Scheme":
    "https",
    "Path":
    "/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=REPLACE",
    "Upgrade-Insecure-Requests":
    "1",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36",
    "DNT":
    "1",
    "Accept":
    "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":
    "gzip, deflate, br",
    "Accept-Language":
    "en-CA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}

session = None
driver = None

def grab_url_request(url, headers=DEFAULT_HEADERS, params=None, return_soup=False, webdriver=False):
    global session
    global driver

    if webdriver:
        if not driver:
            options = webdriver.ChromeOptions()
            # options.add_argument("headless")  # remove this line if you want to see the browser popup
            driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    else:
        if not session:
            session = requests.Session()
        if params:
            r = session.get(url, params=params, headers=headers)
        else:
            r = session.get(url, headers=headers)

        if return_soup:
            soup = BeautifulSoup(r.text, 'html.parser')
            return (soup, r)
        return r


def close():
    global driver
    if driver:
        driver.quit()


def fetch_new_review_info(thread_id, book_url):
    '''
    Returns {
        name: string,
        review: string | NONE,
        rating: int | NONE,
        amazon_user_id: int | NONE, 
    } | None
    '''
    try:
        soup, r = grab_url_request(book_url, return_soup=True)

        if r.status_code != 200:
            print(f'[Thread {thread_id}] Non 200 Return Code', book_url, r)
            return None

        name = []
        for n in soup.select('.a-profile-name span'):
            name.append(n.text)

        rating = None
        rating_node = soup.select('#dp-cmps-expand-header-last .a-icon-alt')
        if len(rating_node) == 1:
            if 'out' in rating_node[0].text:
                rating = float(rating_node[0].text.split(' ')[0])

        review = None
        review_node = soup.select('.review-data div')
        if len(review_node) > 0:
            for node in review_node:
                if not node.has_attr('class'):
                    review = node.text

        return {
            "name": name,
            "rating": rating,
            "review": review,
            "amazon_user_id": None,
        }
    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', book_url, error)
        return None