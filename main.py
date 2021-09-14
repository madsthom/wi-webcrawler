from crawler.Crawler import Crawler

if __name__ == "__main__":
    crawler = Crawler(["https://en.wikipedia.org/wiki/Scheme_(programming_language)"])
    crawler.crawl()
