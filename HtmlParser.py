import requests
from bs4 import BeautifulSoup


def find_valid_urls(a_tags):
    valid_urls = []
    for a in a_tags:
        if a.has_attr('href') and a['href'].startswith('https://'):
            valid_urls.append(a['href'])
    return valid_urls


def query_html(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_title(parsed_html):
    title_tag = parsed_html.find('title')

    if title_tag:
        return title_tag.text
    else:
        return "No title found"


def extract_links_from(url: str):
    parsed_html = query_html(url)
    a_tags = parsed_html.find_all('a')
    return find_valid_urls(a_tags)
