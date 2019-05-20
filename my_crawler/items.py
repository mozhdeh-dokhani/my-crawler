#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/04/12
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
import scrapy
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
class MyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    url       = scrapy.Field()
    category  = scrapy.Field()
    reference = scrapy.Field()
    title     = scrapy.Field()
    subTitle  = scrapy.Field()
    body      = scrapy.Field()
    pass
#---------------------------------------------------------------------------------

# https://doc.scrapy.org/en/latest/topics/items.html