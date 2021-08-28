import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = [
        # "dmoz.org"
        "news.baidu.com"
    ]
    start_urls = [
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
        "http://news.baidu.com/"
    ]

    # def parse(self, response):
    #     filename = response.url.split("/")[-2]
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)


    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         title = sel.xpath('a/text()').extract()
    #         link = sel.xpath('a/@href').extract()
    #         desc = sel.xpath('text()').extract()
    #         print(title, link, desc)

    # def parse(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item

    def parse(self, response):
        for sel in response.xpath('//ul/li/strong'):
            item = DmozItem()
            item['title'] = sel.xpath('.//a/text()').extract()
            # item['link'] = sel.xpath('.//a/@href').extract()
            # item['desc'] = sel.xpath('.//text()').extract()
            yield item
        for sel in response.xpath('//ul/li'):
            item = DmozItem()
            item['title'] = sel.xpath('.//a/text()').extract()
            # item['link'] = sel.xpath('.//a/@href').extract()
            # item['desc'] = sel.xpath('.//text()').extract()
            yield item
        print(item['title'])
        pass