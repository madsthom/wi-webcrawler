from crawler.Crawler import Crawler
from helpers.NlpHelper import tokenize, stem, normalize, remove_stopwords
from helpers.PickleHelper import load_list, diff_list

if __name__ == "__main__":
    index = {}
    crawler = Crawler(["https://www.intern.aau.dk/"])
    crawled_stuff = crawler.crawl()
    diff_list(crawled_stuff, "crawled_stuff")

    crawled_stuff = load_list("crawled_stuff")

    for title in crawled_stuff:
        tokens = tokenize(title[1])
        tokens = normalize(tokens)
        tokens = remove_stopwords(tokens)
        stemmed_tokens = stem(tokens)
        for stemmed_token in stemmed_tokens:
            if stemmed_token in index:
                index[stemmed_token].append(title[0])
            else:
                index[stemmed_token] = [title[0]]
    print(index)
