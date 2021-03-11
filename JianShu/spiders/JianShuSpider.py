import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from JianShu.items import JianShuItem
import time
import json


class JianShu(CrawlSpider):
    name = 'JianShu'
    # allowed_domains = ['JianShuSpider.toscrape.com']
    # start_urls = ['https://www.jianshu.com/recommendations/collections?page=1&order_by=hot']
    # start_urls = ['https://book.douban.com/']
    # start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0']

    """
    
        def parse(self, response):
        item = JianShuItem()
        selector = Selector(response)
        print(response)

        infos = selector.xpath('//div[@class="collection-wrap"]')
        print(infos)
        for info in infos:
            title = info.xpath('a[1]/h4/text()').extract()[0]
            content = info.xpath('a[1]/p/text()').extract()
            article = info.xpath('div/a/text()').extract()[0]
            fans = info.xpath('div/text()').extract()[0]
            if content:
                content = content[0]
            else:
                content = ''
            item['title'] = title
            item['content'] = content
            item['article'] = article
            item['fans'] = fans
            yield item
        urls = ['https://www.jianshu.com/recommendations/collections?page={0}&order_by=hot'.format(str(page)) for
                page in range(2, 3)]

        for url in urls:
            yield Request(url, meta={'item': item}, dont_filter=True, callback=self.parse)
        
        
        
        
        
            def parse(self, response):
        item = JianShuItem()
        selector = Selector(response)
        print(response)

        infos = selector.xpath('//div[@class="carousel"]//li')
        print(infos)
        for info in infos:
            print(info)
            title = info.xpath('div[@class="info"]/div[@class="title"]/a/text()').extract()[0]
            content = info.xpath('div[@class="info"]/div[@class="more-meta"]/p[2]/text()').extract()[0]
            article=info.xpath('div[@class="cover"]/a/img/@src').extract()[0]
            item['title'] = title
            item['content'] = content
            item['article'] = article

            yield item
    
    """

    def start_requests(self):
        headers = {
            "Content-Type":"application/json;charset=UTF-8",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
            "token": "oEseQJSix/cqE2Xb3GE3xEuVjuSIL2bAg+oDeE/dSLylJLLWsAHmUsx/2vru/+10GyWx07yJE8gLy6ak6mXkmcLNWCyiL2TkKGF0yKl2IQbkv3bUTi9+BRggR9dBedOh6G3WUt4zFcMLiEsSR4/vUYGUeLeXNOMxlgz17nKN3YhKDmlIwl3FnYNKbq6NRRnTt+FfUAviV4rvgnnr1ogszhhXp/+GakIvvPJMzfERpaNoxw0IRsmE/IAb3OMqz6DXwbHHYxXURrEbvPWWwlWHspLhw6oGF2AQssjUAV9wnF8nl9UBM46KA+Zl4N5jIS7CmmpCeX8lt7PvGZiV3zbtvVsiTQsFxYeSwtOHHHUkakYXzbG5WxPRMy4OLmcaMMJSbAsKzwCa/p0VmoRBBTcjvMsYYBUtz2zTayAH6ptA0Nw="
        }
        url = 'http://test.shulanchina.cn/api/market/advertMerge/advertList'
        pageNumbers=[ i for i in range(1,10)]

        for pageNumber in pageNumbers:
           data={
                "pageNumber": pageNumber,
                "pageSize": 100
           }
           yield scrapy.Request(url=url, method="POST",headers=headers, body=json.dumps(data),dont_filter=True, callback=self.parse)

    def parse(self, response):
        item = JianShuItem()
        print(type(response.text))
        res = json.loads(response.text)
        print(type(res))

        subjects = res['data']['data']
        print(response.text)
        for subject in subjects:
            item['title'] = subject['advertName']
            item['content'] = subject['advertId']
            item['article'] = subject['totalAdvertBudget']
            yield item
