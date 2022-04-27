import scrapy

from scrapy.spiders import Spider


class some_crawler(Spider):
    name = 'some_crawler'

    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def from_crawler(cls, name, *args, **kwargs ):
        spider = cls(*args, **kwargs)
        spider._set_crawler(name)
        return spider

    def start_requests(self):
        urls = ['http://example.com']
        if not urls and hasattr(self, 'urls'):
            raise AttributeError(
                "Crawling could not start: 'start_urls' not found "
                "or empty (but found 'start_url' attribute instead, "
                "did you miss an 's'?)")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


