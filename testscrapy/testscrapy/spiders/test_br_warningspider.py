import scrapy

class TestBrWarning(scrapy.Spider):
    name = "test_br_warning"

    def start_requests(self):
        url = 'http://localhost:8050'  # A valid url to the computer localhost
        yield scrapy.Request(url=url, callback=self.parse, headers={"ACCEPT-ENCODING": "br"})

    def parse(self, response):
        filename = f'BrWarningData.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')