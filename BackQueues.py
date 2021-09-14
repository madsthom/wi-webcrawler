from dataclasses import dataclass

from UrlParser import get_hostname


@dataclass
class BackQueues:
    def __init__(self):
        self.back_queues = {}

    def add_urls(self, new_urls: list):
        for url in new_urls:
            self.add_url(url)

    def add_url(self, url):
        hostname = get_hostname(url)
        if hostname in self.back_queues:
            self.back_queues[hostname].append(url)
        else:
            self.add_queue(hostname, [url])

    def add_queue(self, hostname, url_queue):
        self.back_queues[hostname] = url_queue

    def get_queue(self, hostname):
        if hostname in self.back_queues.keys():
            return self.back_queues[hostname]
        return []

    def remove_queue(self, hostname):
        self.back_queues.pop(hostname)
