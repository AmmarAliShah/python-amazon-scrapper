from requests_html import HTMLSession

class Reviews:
    def _init_(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        self.url = f''

    def pagination(self, page):
        r = s.get(url + str(page))
