import scrapy
import hashlib

from tutorial.items import ListItem


class p2pblackSpider(scrapy.Spider):
    name = "p2pblack"
    allowed_domains = ["p2pblack.com"]
    start_urls = [
        "http://www.p2pblack.com",
    ]

    def parse(self, response):

            for sel in response.xpath('//div[@class="index_blackname_left"]/p'):
                item = ListItem()
                item['name'] = sel.xpath('a/span[@class="index_blk1"]/text()').extract()
                item['id_number'] = sel.xpath('a/span[@class="index_blk2"]/text()').extract()
                item['money'] = sel.xpath('a/span[@class="index_blk3"]/text()').extract()
                item['benjin'] = sel.xpath('a/span[@class="index_blk4"]/text()').extract()
                item['state'] = sel.xpath('a/span[@class="index_blk5"]/text()').extract()
                item['stage'] = sel.xpath('a[@class="index_blk6"]/text()').extract()
                item['_id'] = hashlib.sha1(str(item['id_number'])).hexdigest()
                yield item
