from crawler.Crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler(["https://github.com/"])
    crawler.crawl()
