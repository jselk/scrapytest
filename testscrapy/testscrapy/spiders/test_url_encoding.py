import scrapy

class TestURLEncoding(scrapy.Spider):
    name = "test_url_encoding"

    def start_requests(self):
        urls = [
            # Test to pass:
            'http://google.com/"hello"',  # User-provided example
            'http://google.com/\'goodbye\'',  # Use of escape characters to allow apostrophes
            'http://google.com/\\\'goodmorning\'\\',  # Use of additional escape characters
            'http://youtube.com/"goodnight"',  # A different url
            'http://google.com/hello again',  # A space character within the url
            'http://localhost:8050',  # A valid url to the computer localhost
            'http://google.com/#*%(&%*%$(#(',  # Nonsensical special characters
            'http://sgn32gd####oger.com',  # A more random url
            'http://{1,2}[0]||>:<+',  # Various characters typically used to format strings
            'http://hgnsd#852NQjwdqK*37',  # A random string
            'http://\\\\\\\\\\\\\\\\\\\\',  # ONLY ESCAPE CHARACTERS
            'http://',  # No url / an empty url
            'http://g{}uwuw\'er oie \\.a\'qr1@8h4t0y0',  # An absolute mess of characters
            'http://sys.exit(0)',  # A python statement to crash the program if run as code
            'http://(int)',  # Another statement to confuse the interpreter if run as code
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_encode=True, dont_filter=True)
            # dont_filter enabled for ease of display

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log(f'Saved file {filename}')