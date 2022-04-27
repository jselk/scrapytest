from http.server import BaseHTTPRequestHandler, HTTPServer
import scrapy
from scrapy.crawler import CrawlerProcess
from multiprocessing import Process
import time
import brotli

hostname = "localhost"
port = 8050


class TestServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        #self.send_header("ACCEPT-ENCODING", "br")
        self.end_headers()

        self.wfile.write(brotli.compress(bytes("<html><head><title>TestServer.com</title></head>", "br")))
        self.wfile.write(brotli.compress(bytes("<p>TestWebServer</p>", "br")))
        self.wfile.write(brotli.compress(bytes("<body>", "br")))
        self.wfile.write(brotli.compress(bytes("<p>If you can read this, this data is uncompressed</p>", "br")))
        self.wfile.write(brotli.compress(bytes("</body></html>", "br")))

        print("Server setup success")


class TestBrWarning(scrapy.Spider):
    name = "testbr"

    def start_requests(self):
        url = "http://localhost/"
        yield scrapy.Request(url=url, callback=self.parse)
        # headers = {"ACCEPTED-ENCODING": "br"}
        # dont_filter enabled for ease of display

    def parse(self, response):
        filename = 'WebServerMessage'
        with open(filename, 'wb') as f:
            f.write(response.body)
        print("Accessed server successfully \n \n \n \n")
        self.log(f'Saved file {filename}')


def run_server():
    # Starts python webServer
    webServer = HTTPServer((hostname, port), TestServer)
    print(f'Started server {hostname} on port {port}')

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    # Closes server
    webServer.server_close()
    print(f'Server stopped on port {port}')


def run_client():
    # Runs client spider to request from webServer
    client_process = CrawlerProcess()
    client_process.crawl(TestBrWarning)

if __name__ == "__main__":
    client = Process(target=run_client)
    server = Process(target=run_server)
    client.start()
    server.start()









