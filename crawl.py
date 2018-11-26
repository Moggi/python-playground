# From Udacity: Intro to Computer Science
import requests
from pprint import pprint

url = 'https://google.com.br/'
# url = 'https://github.com/requests/requests'
# url = 'http://docs.python-requests.org/en/master/'
# url = 'https://udacity.github.io/cs101x/index.html'
url = 'https://blog.github.com'


def get_page(url):
    return requests.get(url)


def get_next_url(page):
    marker = '<a href'
    marker_position = page.find(marker)
    if marker_position < 0:
        return None, 0
    start_quote = page.find('"', marker_position)
    # if start_quote < 0:
    #     return None, 0
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


def start_crawler(links, visited_links):
    not_visited_link = []
    while len(links) and len(visited_links) < 20:
        link = links.pop()
        if link in visited_links or link in not_visited_link:
            continue
        try:
            page = get_page(link)
            if page.status_code != 200:
                raise Exception(page.status_code)
            visited_links.append(link)
            links.extend(get_all_links(page.text))
        except Exception:
            not_visited_link.append(link)

    return not_visited_link


links = [url]
visited_links = []
not_visited_link = []

print('Starting Crawler')
not_visited_link = start_crawler(links, visited_links)

print('\nVisited Links:')
pprint(visited_links)
print('\nNot visited Links:')
pprint(not_visited_link)
