import scrapy
# from scrapy.crawler import CrawlerProcess

class CloseSpider(scrapy.Spider):
    name = 'test_close'
    start_urls = ['http://example.com']

    def __init__(self, *args, **kwargs):
        self.timeout = int(kwargs.pop('timeout', '60'))
        super(CloseSpider, self).__init__(*args, **kwargs)

    def start_requests(self):
        urls = ['http://example.com']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {'text': quote.css('span.text::text').get()}

    def stop(self):
        self.crawler.engine.close_spider(self, 'timeout')
