from dataclasses import dataclass

from UrlParser import get_hostname


@dataclass
class BackQueues:
    def __init__(self):
        self.back_queues = {}

    def add_urls(self, hostname: str, new_urls: list):
        for url in new_urls:
            if hostname in self.back_queues:
                self.back_queues[hostname].append(url)
            else:
                self.add_queue(hostname, [url])

    def add_queue(self, hostname, url_queue):
        self.back_queues[hostname] = url_queue

    def get_queue(self, hostname):
        if not hostname:
            return []

        if hostname in self.back_queues:
            return self.back_queues[hostname]

        return []
