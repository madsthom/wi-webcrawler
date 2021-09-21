import requests
from bs4 import BeautifulSoup


def find_valid_urls(a_tags):
    valid_urls = []
    for a in a_tags:
        if a.has_attr('href') and a['href'].startswith('https://'):
            valid_urls.append(a['href'])
    return valid_urls


def query_html(url):
    try:
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')
    except:
        return ""


def get_title(parsed_html):
    title_tag = parsed_html.find('title')

    if title_tag:
        return title_tag.text
    else:
        return "No title found"


def extract_links_from(parsed_html):
    a_tags = parsed_html.find_all('a')
    return find_valid_urls(a_tags)


def extract_links_from_bs4(bs4):
    a_tags = bs4.find_all('a')
    return find_valid_urls(a_tags)
