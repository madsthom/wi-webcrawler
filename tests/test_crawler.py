import unittest

from bs4 import BeautifulSoup

from crawler.Crawler import Crawler


class CrawlerTests(unittest.TestCase):
    def test_extract_urls(self):
        crawler = Crawler([])
        with open('recordings/test_site.html', 'r') as html_file:
            valid_urls = crawler.extract_urls(BeautifulSoup(html_file.read(), 'html.parser'))
            self.assertEqual(len(valid_urls), 2)
            self.assertListEqual(valid_urls, ["https://www.aau.dk/", "https://www.humanrisks.com/"])


if __name__ == '__main__':
    unittest.main()
