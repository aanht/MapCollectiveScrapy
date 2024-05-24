import scrapy

class SustpdfSpider(scrapy.Spider):
    name = "sustpdf"
    allowed_domains = ["corporate.ford.com"]
    start_urls = ["https://corporate.ford.com/social-impact/sustainability/integrated-report-additional-documents.html"]

    def parse(self, response):
        for pdf in response.css('.pdf-element'):
            title = pdf.css('h3::text').get()
            link = response.urljoin(pdf.css("a::attr(href)").get())
            yield {
                'title': title,
                'file_urls': [link]
            }