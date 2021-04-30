# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class WallPaperItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()
    next_page = scrapy.Field()
