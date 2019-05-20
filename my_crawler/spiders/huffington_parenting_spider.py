#------------------------- Mozhdeh Dokhani ---------------------------------------
# date:    97/04/19
# version: 1.0
#---------------------------------------------------------------------------------

#------------------------------- Libraries ---------------------------------------
import scrapy
from my_crawler.items import MyCrawlerItem
from scrapy.spiders import CrawlSpider,Rule
from my_crawler.functions import *
#---------------------------------------------------------------------------------

#------------------------------------ Main ---------------------------------------
class huffingtonParentingSpider(CrawlSpider):
   name            = "huffington_parenting"
   user_agent      = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
   allowed_domains = ["www.huffingtonpost.com"]
   baseURL1        = "https://www.huffingtonpost.com"
   start_urls      = []
   for page in range(1, 6):
      start_urls.append("https://www.huffingtonpost.com/section/parents?page=" + str(page))

   def parse(self, response):
      for url in response.xpath('//div[@class="card__headline"]/a/@href').extract():
         yield scrapy.Request(self.baseURL1 + url, callback = self.parse_item)

   def parse_item(self, response):
      item              = MyCrawlerItem()
      item['url']       = str(response.url)
      item['category']  = 'parenting'
      item['reference'] = 'huffingtonPost'
      item['title']     = str(response.xpath('//h1[@class="headline__title"]//text()').extract()[0])
      item['title']     = processText(item['title'], True, True)
      subTitle          = response.xpath('//h1[@class="headline__title"]');
      item['subTitle']  = ''
      if subTitle:
         item['subTitle'] = str(subTitle.xpath('text()').extract()[0])
         item['subTitle'] = processText(item['subTitle'], True, True)
      # Put the list in a string
      item['body']      = ' '.join([x.strip() for x in (response.xpath('//div[contains(@class, "entry__text") and not(contains(@class, "advertisement"))]//text()[not(ancestor::div/@class="advertisement repeating_dynamic_display")]').extract())])
      item['body']      = processText(item['body'],True,True,True,True)

      yield item
# ---------------------------------------------------------------------------------
