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


def fetch_review_data(thread_id, info):
    try:
        soup, r = grab_url_request(info[1], return_soup=True)

        if r.status_code != 200:
            print(f'[Thread {thread_id}] Non 200 Return Code', info, r)
            return None

        data = []
        name = None
        rating = None
        review = None
    
        review_node = soup.select('.review')
        print("book_url: ", info[1])

        if len(review_node) > 0:
            for r in review_node:
                name = r.select('.a-profile-name')[0].text
                user_id = r.select('div a')[0]['href'].strip().split('.', 2)[2].split('/', 1)[0]
                rating = float(r.select('.a-icon-alt')[0].text.split(' ')[0])
                review = r.select('div .review-data')[1].text.split('Read more', 1)[0]

                data.append({"book_id": info[0],
                            "user_id": user_id,
                            "name":  name,
                            "rating": rating,
                            "review": review})

        return data
    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', info[1], error)
        return None

if __name__ == "__main__":
    book_url = "https://www.amazon.ca/Constants-Nature-Omega-Numbers-Universe/dp/0375422218/"
    print(fetch_review_data(1, [1, book_url]))