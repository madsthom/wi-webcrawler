from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

from BackQueues import BackQueues
from Frontier import Frontier
from UrlParser import get_hostname


class Crawler:
    def __init__(self, seeds):
        self.frontier = Frontier(seeds)
        self.back_queues = BackQueues()
        self.heap = []

    @staticmethod
    def crawl_allowed(url):
        try:
            print(url)
            rp = RobotFileParser()
            rp.set_url(url)
            rp.read()
            return rp.can_fetch("*", url)
        except:
            return False

    @staticmethod
    def extract_urls(doc: BeautifulSoup):
        a_tags = doc.find_all('a')

        valid_urls = []

        for a in a_tags:
            if a.has_attr('href') and a['href'].startswith('https://'):
                valid_urls.append(a['href'])
        return valid_urls

    @staticmethod
    def query_html(url):
        response = requests.get(url)
        return BeautifulSoup(response.text, 'html.parser')

    def crawl(self):
        while len(self.frontier) > 0:
            url = self.frontier.get_url()
            if self.crawl_allowed(url):
                hostname = get_hostname(url)
                parsed_html = self.query_html(url)
                new_urls = self.extract_urls(parsed_html)

                self.back_queues.add_urls(hostname, new_urls)
