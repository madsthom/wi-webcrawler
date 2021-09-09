from Crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler(["https://www.aau.dk/", "https://www.humanrisks.com/"])
    crawler.crawl()
