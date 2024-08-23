import scrapy


class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["lu.ru"]
    start_urls = ["https://lu.ru/rasprodazhi/ucenka/"]

    def parse(self, response):
        lights = response.css('div.product-block')
        for light in lights:
            yield {
                'name' : light.css('div.product-name-block span::text').get(),
                'price' : light.css('div.new-price span::text').get(),
                'url' : light.css('a').attrib['href']
            }
