import requests
import urllib
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import base64

AMAZON_SEARCH_URL = 'https://www.amazon.ca/s/ref=nb_sb_noss'
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


def search_amazon_for_review(thread_id, book_title, book_author):
    '''
    Search amazon for the book by that author, grab the first link and return that url or None

    Returns string | None
    '''
    global driver
    try:

        url = AMAZON_SEARCH_URL + '?' + urllib.parse.urlencode({
            'url': 'search-alias=stripbooks',
            'field-keywords': book_title + ' by ' + book_author
        })
        # print(url)

        soup, re = grab_url_request(url, return_soup=True, webdriver=True)

        p = re.compile(r"/[a-zA-Z\-]+/dp/[0-9]+/")

        all_links = soup.select('a')
        count_links = 0
        print(f'Number of links found via soup: {len(all_links)}')
        for a in all_links:
            if not a.has_attr('href'):
                continue
            
            # print(a['href'])
            count_links += 1
            m = p.search(a['href'])
            if m:
                if a['href'].startswith('/'):
                    return 'https://www.amazon.ca' + a['href']
                return a['href']

        print(f'[Thread {thread_id}] ERROR: Could not find any results for {book_title} by {book_author} ' +
              f'when searching {len(all_links)} links, and processing {count_links} links')
        # print(soup.prettify())
        return None

    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to search for', book_title, error)
        return None


def fetch_new_review_info(thread_id, book_url):
    '''
    Returns {
        review_id: string,
        amazon_user_id: string,
        book_id: int,
        rating: int | NONE,
        review: string | NONE,
    } | None
    '''
    try:
        soup, r = grab_url_request(book_url, return_soup=True)

        if r.status_code != 200:
            print(f'[Thread {thread_id}] Non 200 Return Code', book_url, r)
            return None

        review_id = []
        amazon_user_id = []
        review = None
        rating = None

        details_node = soup.select('#cm-cr-dp-review-list')
        if len(details_node) > 0:
            for node in details_node:
                for sub in node.select('div'):
                    #review_id
                    review_id.append(sub['id'])

                    #amazon_user_id
                    amazon_user_id = sub.select('a')['href']

                    #rating
                    rating_node = sub.select('a-icon-alt')
                    if len(rating_node) == 1:
                        if 'out' in rating_node[0].text:
                            rating = float(rating_node[0].text.split(' ')[0])
    
                    #review
                    review = sub.select('.review_text div div').text

        return {
            "review_id": review_id,
            "amazon_user_id": amazon_user_id,
            "rating": rating,
            "review": review,
        }
    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', book_url, error)
        return None