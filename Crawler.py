from urllib.robotparser import RobotFileParser

import requests
from bs4 import BeautifulSoup

from Frontier import Frontier
from QueueManager import QueueManager


# TODO:
# - Heap should be a class
# - Look at what exceptions get thrown

class Crawler:
    def __init__(self, seeds):
        self.frontier = Frontier(seeds)
        self.queue_manager = QueueManager()

    @staticmethod
    def crawl_allowed(url):
        try:
            rp = RobotFileParser()
            rp.set_url(url)
            rp.read()
            return rp.can_fetch("*", url)
        except:
            return False

    def extract_urls(self, url: str):
        parsed_html = self.query_html(url)
        a_tags = parsed_html.find_all('a')

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
                new_urls = self.extract_urls(url)
                self.queue_manager.add_to_back_queue(new_urls)

            if len(self.frontier) == 0:
                new_host = self.queue_manager.heap_pop()
                back_queue = self.queue_manager.get_queue(new_host)
                self.frontier.add(back_queue.pop(0))

                if len(back_queue) == 0:
                    self.queue_manager.remove_queue(new_host)
                else:
                    self.queue_manager.heap_push(new_host)


