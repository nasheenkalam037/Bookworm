import requests
import re
from bs4 import BeautifulSoup

AMAZON_SEARCH_URL = 'https://www.amazon.ca/s/ref=nb_sb_noss?url=search-alias%3Dstripbooks&field-keywords=REPLACE'
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


def grab_url_request(url, headers=DEFAULT_HEADERS, return_soup=False):
    with requests.Session() as s:
        r = s.get(url, headers=headers)

    if return_soup:
        return BeautifulSoup(r.text, 'html.parser'), r
    return r


# TODO complete search_amazon_for_book()
def search_amazon_for_book(thread_id, book_title, book_author):
    '''
    Search amazon for the book by that author, grab the first link and return that url or None

    Returns string | None
    '''
    pass


# TODO complete fetch_new_book_info()
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
            if 'out' in price_node[0].text:
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

        details_node = soup.select('.content')
        if len(details_node) == 1:
            text = details_node[0].text

            # PAGES
            p = re.compile(r'([0-9]+) pages')
            m = p.search(text)
            if m:
                pages = int(m.group(1))

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
                "synopsis": synopsis,
                "price": price,
            },
            "authors": authors,
            "categories": categories
        }
    except Exception as error:
        print(f'[Thread {thread_id}] An Error occurred while trying to read from', book_url, error)
        return None