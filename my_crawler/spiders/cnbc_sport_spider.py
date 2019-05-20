#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/04/26
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
import scrapy
from my_crawler.items import MyCrawlerItem
from scrapy.spiders import CrawlSpider,Rule
from my_crawler.functions import *
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
class cnbcSportSpider(CrawlSpider):
   name            = "cnbc_sport"
   user_agent      = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
   allowed_domains = ["www.cnbc.com"]
   baseURL1        = "https://www.cnbc.com"
   start_urls      = []
   for page in range(1, 105):
      start_urls.append("https://www.cnbc.com/sports-business/?page=" + str(page))

   def parse(self, response):
      for url in response.xpath('//div[@id="pipeline"]//div[contains(@class, "headline")]/a/@href').extract():
         yield scrapy.Request(self.baseURL1 + url, callback = self.parse_item)

   def parse_item(self, response):
      item              = MyCrawlerItem()
      item['url']       = str(response.url)
      item['category']  = 'sport'
      item['reference'] = 'cnbc'
      item['title']     = str(response.xpath('//meta[@name="twitter:title"]/@content').extract()[0])
      item['title']     = processText(item['title'],True,True)
      item['subTitle']  = str(response.xpath('//meta[@itemprop="description"]/@content').extract()[0])
      item['subTitle']  = processText(item['subTitle'], True, True)
      # Put the list in a string
      item['body']      = ' '.join([x.strip() for x in (response.xpath('//div[@id="article_body"]//text()').extract())])
      item['body']      = processText(item['body'],True,True,True)

      if ( item['body'] != "" ):
         yield item
# ---------------------------------------------------------------------------------
