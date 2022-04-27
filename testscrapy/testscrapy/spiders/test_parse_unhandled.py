import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from urllib.parse import urlparse


class ParseSpider(scrapy.Spider):
    name = 'test_parse'

    def start_requests(self):
        urls = [
            'http://www.baidu.com',
        ]
        for url in self.start_urls:
            url_1 = 'http://www.baidu.com'
            link = urllib.urlopen(url_1)
            link_open = link.read()
            request = Request(url, dont_filter=True)
            print (self.start_urls)
            yield request

    def parse(self, response):
        print("URL: " + link_open + request)

