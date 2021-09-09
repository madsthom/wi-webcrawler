import urllib.parse


def parse_url(url):
    return urllib.parse.urlparse(url)


def get_hostname(url):
    parsed_url = urllib.parse.urlparse(url)
    return parsed_url.hostname
