import requests
import urllib
import re
import sys
import traceback
import base64
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=REPLACE'
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


def grab_url_request(url, headers=DEFAULT_HEADERS, params=None, return_soup=False, use_webdriver=False):
    global session
    global driver

    if use_webdriver:
        if not driver:
            chrome_options = Options()
            chrome_options.add_argument("--log-level=3")
            # options.add_argument("headless")  # remove this line if you want to see the browser popup
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


def close():
    global driver
    if driver:
        driver.quit()


def search_amazon_for_book(thread_id, book_title, book_author):
    '''
    Search amazon for the book by that author, grab the first link and return that url or None

    Returns string | None
    '''
    try:

        url = AMAZON_SEARCH_URL + '?' + urllib.parse.urlencode({
            'url': 'search-alias=stripbooks',
            'field-keywords': book_title + ' by ' + book_author
        })
        # print(url)

        soup = grab_url_request(url, return_soup=True, use_webdriver=True)

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
        traceback.print_exc(limit=2, file=sys.stdout)
        return None


def fetch_new_book_info(thread_id, book_url):
    '''
    Returns {
        title: string,
        series: string | NONE,
        series_position: int | NONE,
        pages: int | NONE,
        publisher: string | NONE,
        orig_published_date: string | NONE,
        isbn10: string | NONE,
        isbn13: string | NONE,
        synopsis: string | NONE,
        amazon: {
            book_link: string,
            rating: decimal | NONE,
            synopsis: string | NONE,
            price: decimal | NONE,
        }
        authors: [string, ...], 
        categories: [string, ...], 
    } | None
    '''

    try:
        soup, r = grab_url_request(book_url, return_soup=True)

        if r.status_code != 200:
            print(f'[Thread {thread_id}] Non 200 Return Code', book_url, r)
            return None

        title = soup.select('#productTitle')[0].text

        authors = []
        for a in soup.select('.author a'):
            authors.append(a.text)

        categories = set()
        for c in soup.select('.zg_hrsr_ladder'):
            for a in c.select('a'):
                categories.add(a.text)

        rating = None
        rating_node = soup.select('#averageCustomerReviews .a-icon-alt')
        if len(rating_node) == 1:
            if 'out' in rating_node[0].text:
                rating = float(rating_node[0].text.split(' ')[0])

        price = None
        price_node = soup.select('.offer-price')
        if len(price_node) > 0:
            if '$' in price_node[0].text:
                price = float(price_node[0].text.split(' ')[1])

        synopsis = None
        synopsis_node = soup.select('noscript div')
        if len(synopsis_node) > 0:
            for node in synopsis_node:
                if not node.has_attr('class'):
                    synopsis = node.text

        pages = None
        isbn10 = None
        isbn13 = None
        publisher = None
        orig_published_date = None
        num_reviews = None

        details_node = soup.select('.content')
        if len(details_node) == 1:
            text = details_node[0].text

            # PAGES
            p = re.compile(r'([0-9]+) pages')
            m = p.search(text)
            if m:
                pages = int(m.group(1))
            # Number of Reviews
            p = re.compile(r'([0-9]+)\s*customer review')
            m = p.search(text)
            if m:
                num_reviews = int(m.group(1))
            # PUBLISHER & DATE
            p = re.compile(r'Publisher:\s*([\w\s]+)\(([\w\s]+)\)')
            m = p.search(text)
            if m:
                publisher = m.group(1).strip()
                orig_published_date = m.group(2).strip()
            # ISBN10
            p = re.compile(r'ISBN-10:\s*([0-9]+)')
            m = p.search(text)
            if m:
                isbn10 = m.group(1)
                if len(isbn10) > 10:
                    print('[Thread {thread_id}] Incorrect ISBN10 number:', isbn10)
                    isbn10 = None
            # ISBN13
            p = re.compile(r'ISBN-13:\s*([0-9\-]+)')
            m = p.search(text)
            if m:
                isbn13 = m.group(1)

        return {
            "title": title,
            "series": None,
            "series_position": None,
            "pages": pages,
            "publisher": publisher,
            "orig_published_date": orig_published_date,
            "isbn10": isbn10,
            "isbn13": isbn13,
            "synopsis": synopsis,
            "amazon": {
                "book_link": book_url,
                "rating": rating,
                "num_reviews": num_reviews,
                "synopsis": synopsis,
                "price": price,
            },
            "authors": authors,
            "categories": categories
        }
    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', book_url, error)
        return None


def get_amazon_book_cover(thread_id, book_url, filename, folder):
    try:
        soup, r = grab_url_request(book_url, return_soup=True)

        if r.status_code != 200:
            print(f'[Thread {thread_id}] Non 200 Return Code', book_url, r)
            return None

        book_cover_url = soup.select('#imageBlock img')

        if len(book_cover_url) != 1:
            print(f'[Thread {thread_id}] Switching to Chrome because of captcha', book_url)
            soup = grab_url_request(book_url, use_webdriver=True)


        book_cover_url = soup.select('#imageBlock img')

        if len(book_cover_url) == 1:
            data = book_cover_url[0]['src'].strip()
            if data.startswith('data:'):
                data = data.split(':', 1)[1]
                ext = data.split(';', 1)
                data = ext[1]
                ext = ext[0].split('/', 1)[1]

                encoding = data.split(',', 1)
                data = encoding[1]
                encoding = encoding[0]

                if encoding != 'base64':
                    return f'Unknown Encoding {encoding}; with extension {ext}'
                
                img_filename = folder + '/' + str(filename) +'.' + ext
                with open(img_filename, 'wb') as f:
                    f.write(base64.b64decode(data))
            else:
                return 'Dealing with a src that is not embedded!'
        else:
            return 'Could Not find any book cover!'

        return ''
    except Exception as error:
        return f'[Thread {thread_id}] An Error occurred while trying to read from: {book_url} with error: {error}'


if __name__ == "__main__":
    get_amazon_book_cover(1, 'https://www.amazon.ca/Clariel-Lost-Abhorsen-Garth-Nix/dp/0061561576/ref', 'test', '')