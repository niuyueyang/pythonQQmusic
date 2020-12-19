# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QqmusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_name = scrapy.Field()  # 歌曲
    album_name = scrapy.Field()  # 唱片
    singer_name = scrapy.Field()  # 歌手
    interval = scrapy.Field()  # 时长
    pass
