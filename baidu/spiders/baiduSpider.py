# -*- coding: utf-8 -*-
import scrapy
from baidu.items import BaiduItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    allowed_domains = ['cnblogs.com']
    start_urls = ['https://www.cnblogs.com/#p1']
    rules = (
        Rule(LinkExtractor(allow=r'/#p/[0-9]{1,20}'), callback='parse', follow=True),
    )
    def parse(self, response):
        item_list = response.xpath("//div[@class='post_item']")
        for item in item_list:
            blogItem = BaiduItem()
            # blogItem['title'] = item.xpath('./div[2]/h3[1]/a/text()')[0].extract().strip()
            # blogItem['titleLink'] = item.xpath('./div[2]/h3[1]/a/@href')[0].extract()
            # blogItem['suggestNum'] = item.xpath('./div[1]/div[1]/span/text()')[0].extract().strip()
            # content = item.xpath('./div[2]/p[1]/text()')
            # for c in content:
            #     if c.extract().strip() != '':
            #         blogItem['content'] = c.extract().strip()
            #     else:
            #         blogItem['content'] = ''
            # blogItem['author'] = item.xpath('./div[2]/div[1]/a/text()')[0].extract().strip()
            # blogItem['publishDate'] = item.xpath('./div[2]/div[1]/text()')[1].extract().strip()
            yield blogItem
        # handle next page
        next=response.xpath("//div[@class='pager']/a[last()]/text()")[0].extract().strip()
        print(next)
        if 'Next' in next:
            nextUrlStr=response.xpath("//div[@class='pager']/a[last()]/@href")[0].extract().strip()
            nextNum = nextUrlStr[-1]
            nextNum=2
            if int(nextNum) < 5:
                nextUrl = 'https://www.cnblogs.com/#p/{0}'.format(nextNum)
                print(nextUrl)
                nextNum +=1
                yield scrapy.Request(nextUrl,callback=self.parse)
