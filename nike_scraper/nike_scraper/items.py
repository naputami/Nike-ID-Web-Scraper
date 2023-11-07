# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NikeScraperItem(scrapy.Item):
    title = scrapy.Field()
    subtitle = scrapy.Field()
    product_url = scrapy.Field()
    img_url = scrapy.Field()
    current_price = scrapy.Field()
    full_price = scrapy.Field()
    discounted = scrapy.Field()