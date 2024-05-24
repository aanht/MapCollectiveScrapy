import scrapy


class PracticeSpider(scrapy.Spider):
    name = "practice"
    allowed_domains = ["www.boschautoparts.com"]
    start_urls = ["https://www.boschautoparts.com/"]

    def parse(self, response):
        for link_href in response.css("a::attr(href)"):
            yield {
                "href": link_href.get()
            }
