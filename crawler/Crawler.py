import socket
from time import sleep
from urllib.robotparser import RobotFileParser

from crawler.Frontier import Frontier
from helpers.HtmlParser import extract_links_from, get_title, query_html
from crawler.QueueManager import QueueManager

DEFAULT_TIMEOUT = 5


# TODO:
# - Look at what exceptions get thrown

class Crawler:
    def __init__(self, seeds):
        self.crawled_urls = []
        self.frontier = Frontier(seeds)
        self.queue_manager = QueueManager()
        self.crawled_titles = []
        socket.setdefaulttimeout(DEFAULT_TIMEOUT)

    @staticmethod
    def crawl_allowed(url):
        rp = RobotFileParser()
        rp.set_url(url)
        rp.read()
        return rp.can_fetch("*", url)

    def visited(self, url):
        return url in self.crawled_urls

    def save_url_entry(self, url):
        self.crawled_urls.append(url)

    def process(self, url):
        parsed_html = query_html(url)
        title = get_title(parsed_html)
        print(title)

        self.crawled_titles.append(title)

        new_urls = extract_links_from(parsed_html)
        self.queue_manager.add_to_back_queues(new_urls)

        self.save_url_entry(url)

    def crawl(self):
        i = 0
        while i < 10:
        #while not self.frontier.empty():
            sleep(1)
            url = self.frontier.get_url()
            if self.crawl_allowed(url) and not self.visited(url):
                self.process(url)
            if self.frontier.empty():
                self.frontier.add(self.queue_manager.get_new_seed())
            i += 1

        # Should not return anything tho, only for test
        return list(zip(self.crawled_urls, self.crawled_titles))
