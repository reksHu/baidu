# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #title
    #//div[@class='post_item']/div[2]/h3[1]/a/text()
    title=scrapy.Field()
    #title link
    #//div[@class='post_item']/div[2]/h3[1]/a/@href
    titleLink=scrapy.Field()
    #sugget num
    #//div[@class='post_item']/div[1]/div[1]/span/text()
    suggestNum=scrapy.Field()
    #content
    #//div[@class='post_item']/div[2]/p[1]/text()
    content=scrapy.Field()
    #author
    #//div[@class='post_item']/div[2]/div[1]/a/text()
    author=scrapy.Field()
    #publish time:
    #//div[@class='post_item']/div[2]/div[1]/text()
    publishDate=scrapy.Field()
