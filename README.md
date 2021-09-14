# Web Crawler Created in the Web Intelligence Course

## Current implementation

The web crawler currently implements

* A Front queue to keep track of seeds
* A simple back queue implementation which keep track of urls form different hostnames
* Url parser helper module

## TODO

- [ ] Heap should also keep track of crawl times (politeness)
- [X] Front queue should be updated when empty by lookup in the heap
- [ ] Tests for Back Queue implementation
- [ ] Tests for url parser helper module (Should be very easy to do)
- [ ] Tests for Crawler class
- [ ] Test for HtmlParser module
- [ ] Crawler should keep going on exceptions (try-catches maybe?)