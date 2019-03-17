import requests
import urllib
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

def grab_url_request(url, headers=DEFAULT_HEADERS, params=None, return_soup=False, use_webdriver=False):
    global session
    global driver

    if use_webdriver:
        if not driver:
            chrome_options = Options()
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_argument("headless")  # remove this line if you want to see the browser popup
            driver = webdriver.Chrome(options=chrome_options)
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
    url = "https://www.amazon.com/product-reviews" + info[1].strip().split('dp')[1]
    
    try:
        soup = grab_url_request(url, return_soup=True, use_webdriver=True)

        # if soup.status_code != 200:
        #     print(f'[Thread {thread_id}] Non 200 Return Code', info, r)
        #     return None

        data = []
        name = None
        rating = None
        review = None
    
        review_node = soup.select('.review')
        print("book_url: ", url)
        print('review_node from book_url: ', len(review_node))

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
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', url, error)
        return None

def fetch_review_from_user_acc(thread_id, book, user_id):
    url = "https://www.amazon.com/gp/profile/amzn1.account." + user_id
    
    try:
        soup = grab_url_request(url, return_soup=True, use_webdriver=True)
        review_node = soup.select('.main #customer-profile-timeline #profile-at-card-container')[0]
        # review_node = soup.select('.main .a-section .a-section')[0]
        # review_node = soup.select('.desktop')
        print(user_id, ' desk: ', len(review_node))
        data = []

        if review_node:
            for r in review_node:
                prod_link = r.select('div')[1].select('.profile-at-content div .profile-at-product-box-link')
                
                if prod_link:
                    prod_id = prod_link[0]['href'].strip().split('dp/')[1].split('?')[0]
                    # print("prod_link: ", prod_link[0]['href'])
                    p = re.compile(r'[0-9]+')
                    
                    book_id_link = None
                    name = None
                    rating = None
                    review = None

                    if p.match(prod_id) != None:
                        print("book_link: ", prod_link[0]['href'])
                        old_book_url = book[1].strip().split('https://www.amazon.ca')[1]
                        if old_book_url in prod_link[0]['href']:
                            book_id_link = book[0]
                        else:
                            book_id_link = "https://www.amazon.ca" + prod_link[0]['href']

                        name = r.select('.a-profile-name')[0].text
                        rating = float(r.select('.profile-at-review-stars span')[0].text.split(' ')[0])
                        review = r.select('.profile-at-review-text-desktop')[0].text
                        
                        data.append({"book_id_link": book_id_link,
                                    "user_id": user_id,
                                    "name":  name,
                                    "rating": rating,
                                    "review": review})
                        
        return data

    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', url, error)
        return None 


if __name__ == "__main__":
    book_url = "https://www.amazon.com/Harry-Potter-Paperback-Box-Books/dp/0545162076/ref=sr_1_1?crid=1NN10PFINJXBU&keywords=harry+potter+books&qid=1552116615&s=gateway&sprefix=Harry%2Caps%2C195&sr=8-1"
    print(fetch_review_data(1, [1, book_url]))