from urllib.robotparser import RobotFileParser

from Frontier import Frontier
from HtmlParser import extract_links_from, get_title
from QueueManager import QueueManager


# TODO:
# - Look at what exceptions get thrown

class Crawler:
    def __init__(self, seeds):
        self.crawled_urls = []
        self.frontier = Frontier(seeds)
        self.queue_manager = QueueManager()
        self.crawled_titles = []

    @staticmethod
    def crawl_allowed(url):
        try:
            rp = RobotFileParser()
            rp.set_url(url)
            rp.read()
            return rp.can_fetch("*", url)
        except:
            return False

    def visited(self, url):
        return url not in self.crawled_urls

    def save_url_entry(self, url):
        self.crawled_urls.append(url)
        self.crawled_titles.append(get_title(url))

    def process(self, url):
        self.save_url_entry(url)

        new_urls = extract_links_from(url)
        self.queue_manager.add_to_back_queues(new_urls)

    def crawl(self):
        while self.frontier.empty():
            url = self.frontier.get_url()
            if self.crawl_allowed(url) and not self.visited(url):
                self.process(url)

            if self.frontier.empty():
                self.frontier.add(self.queue_manager.get_new_seed())
