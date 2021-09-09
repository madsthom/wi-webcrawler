from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

from Frontier import Frontier


class Crawler:
    def __init__(self, seeds):
        self.frontier = Frontier(seeds)

    @staticmethod
    def crawl_allowed(link):
        rp = RobotFileParser()
        rp.set_url(link)
        rp.read()
        return rp.can_fetch("*", link)

    @staticmethod
    def extract_urls(doc: BeautifulSoup):
        a_tags = doc.find_all('a')

        valid_urls = []

        for a in a_tags:
            if a.has_attr('href') and a['href'].startswith('https://'):
                valid_urls.append(a['href'])
        return valid_urls

    def crawl(self):
        while len(self.frontier) > 0:
            link = self.frontier.get_url()
            if self.crawl_allowed(link):
                r = requests.get(link)
                doc = BeautifulSoup(r.text, 'html.parser')
                self.frontier.add(self.extract_urls(doc))
                print(doc.find('title').text)
