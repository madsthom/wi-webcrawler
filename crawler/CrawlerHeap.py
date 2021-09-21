class CrawlerHeap:
    def __init__(self):
        self.heap = []

    def pop(self):
        return self.heap.pop(0)  # If .pop(0) then breadth first

    def push(self, hostname):
        if hostname not in self.heap:
            self.heap.append(hostname)

    def remove(self, hostname):
        self.heap.remove(hostname)

    def __len__(self):
        return len(self.heap)
