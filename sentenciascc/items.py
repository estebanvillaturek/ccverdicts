# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item

class SentenciasccItem(scrapy.Item):
    link = scrapy.Field()
    text = scrapy.Field()
    

   
