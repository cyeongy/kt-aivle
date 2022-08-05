
import scrapy
from gmarket.items import GmarketItem


class GMSpider(scrapy.Spider):
    name = "GMB"
    allow_domain = ["gmarket.co.kr"]
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse_content(self, response):
            item = GmarketItem()
            item['title'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()').extract()
            item['price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()').extract()
            item['link'] = response.url
            yield item

    def parser(self, response):
        links = response.xpath('//*[@id="gBestWrap"]/div/div[3]/div/ul/li/a/@href').extract()
        for link in links[:20]:
            yield scrapy.Request(link, callback=self.parse_content)


