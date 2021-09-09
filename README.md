# Web Crawler Created in the Web Intelligence Course

## Current implementation

The web crawler currently implements

* A Front queue to keep track of seeds
* A simple back queue implementation which keep track of urls form different hostnames
* Url parser helper module

## TODO

- [ ] Implement heap to keep track of crawl times and hostnames
- [ ] Front queue should be updated when empty by lookup in the heap
- [ ] Tests for Back Queue implementation
- [ ] Tests for url parser helper module (Should be very easy to do)
- [ ] Crawler should keep going on exceptions (try-catches maybe?)