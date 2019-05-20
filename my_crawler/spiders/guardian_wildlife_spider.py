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
class guardianWildlifeSpider(CrawlSpider):
   name            = "guardian_wildlife"
   user_agent      = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
   allowed_domains = ["www.theguardian.com"]
   baseURL1        = "https://www.theguardian.com"
   start_urls      = []
   for page in range(1, 665):
      start_urls.append("https://www.theguardian.com/environment/wildlife?page=" + str(page))

   def parse(self, response):
      for url in response.xpath('//h1[contains(@class, "fc-item__title")] | //h2[contains(@class, "fc-item__title")]/a/@href').extract():
         yield scrapy.Request( url, callback = self.parse_item)

   def parse_item(self, response):
      item              = MyCrawlerItem()
      item['url']       = str(response.url)
      item['category']  = 'wildlife'
      item['reference'] = 'guardian'
      item['title']     = str(response.xpath('//h1[contains(@class, "content__headline")] | //h1/span[contains(@class, "content__headline--interview-wrapper")]//text()').extract()[0])
      item['title']     = processText(item['title'],True,True)
      item['subTitle']  = str(response.xpath('//meta[@itemprop="description"]/@content').extract()[0])
      item['subTitle']  = processText(item['subTitle'], True, True)
      # Put the list in a string
      item['body']      = ' '.join([x.strip() for x in (response.xpath('//div[contains(@class, "content__article-body") and not(contains(@class, "submeta"))]//text()[not(ancestor::div/@class="submeta")]').extract())])
      item['body']      = processText(item['body'],True,True,True)

      if ( item['body'] != "" ):
         yield item
# ---------------------------------------------------------------------------------
