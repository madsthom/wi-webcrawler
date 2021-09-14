class CrawlerHeap:
    def __init__(self):
        self.heap = []

    def pop(self):
        return self.heap.pop()

    def push(self, hostname):
        if hostname not in self.heap:
            self.heap.append(hostname)

    def remove(self, hostname):
        self.heap.remove(hostname)
