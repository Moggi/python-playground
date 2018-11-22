# From Udacity: Intro to Computer Science
import requests

url = 'http://docs.python-requests.org/en/master/'


def get_page(url):
    return requests.get(url)


def get_next_url(page):
    marker = '<a href='
    marker_position = page.find(marker)
    if marker_position < 0:
        return None, 0
    start_quote = page.find('"', marker_position)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]
    return url, end_quote


def print_all_links(page):
    while True:
        url, end_pos = get_next_url(page)
        if url:
            print(url)
            page = page[end_pos:]
        else:
            break

page = get_page(url)
page_content = page.text if page.status_code == 200 else ''

print_all_links(page_content)
