from BackQueues import BackQueues
from CrawlerHeap import CrawlerHeap
from UrlParser import get_hostname


class QueueManager:
    def __init__(self):
        self.back_queues = BackQueues()
        self.heap = CrawlerHeap()

    def add_to_back_queue(self, urls):
        for url in urls:
            self.back_queues.add_url(url)
            self.heap_push(get_hostname(url))

    def get_queue(self, hostname):
        return self.back_queues.get_queue(hostname)

    def remove_queue(self, hostname):
        self.back_queues.remove_queue(hostname)

    def heap_pop(self):
        return self.heap.pop()

    def heap_push(self, hostname):
        if hostname not in self.heap.heap: # fix iter
            self.heap.push(hostname)

    def heap_remove(self, hostname):
        self.heap.remove(hostname)
