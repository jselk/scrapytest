import scrapy
class testingurl(scrapy.Spider):

    name = "testurl" # my spider for testing the url encoding problem

    def start_requests(self):
        urls = [
            'http://google.com/???',
            'http://google.com/##'
        ]
        for url in urls:
            bool = False
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'testurl-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
