# From Udacity: Intro to Computer Science
import requests
from pprint import pprint

url = 'http://docs.python-requests.org/en/master/'
url = 'https://udacity.github.io/cs101x/index.html'


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


def get_all_links(page):
    links = []
    while True:
        url, end_pos = get_next_url(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links

links = [url]
visited_links = []

while len(links):
    link = links.pop()
    if link in visited_links:
        continue
    page = get_page(link)
    visited_links.append(link)
    page_content = page.text if page.status_code == 200 else ''
    links += get_all_links(page_content)

pprint(visited_links)
