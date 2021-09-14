from dataclasses import dataclass


@dataclass
class Frontier:
    front_queue = []

    def __init__(self, seeds):
        self.front_queue = seeds

    def get_url(self):
        return self.front_queue.pop(0)

    def add(self, url):
        self.front_queue.append(url)

    def add_urls(self, urls: list):
        self.front_queue.extend(urls)

    def empty(self):
        return len(self.front_queue) == 0

    def __len__(self):
        return len(self.front_queue)
