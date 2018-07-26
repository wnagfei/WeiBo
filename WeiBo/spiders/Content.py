from scrapy import Request, Spider
from urllib.parse import quote
from WeiBo.items import WeiboItem
import urllib
class Content(Spider):
    name = "content"
    urls= ["https://www.weibo.com/u/3202442071?profile_ftype=1&is_ori=1#_0",
            "https://www.weibo.com/u/3202442071?is_search=0&visible=0&is_ori=1&is_tag=0&profile_ftype=1&page=2#feedtop",
            "https://www.weibo.com/u/3202442071?is_search=0&visible=0&is_ori=1&is_tag=0&profile_ftype=1&page=3#feedtop"
        ]
    def start_requests(self):
        for url in  self.urls:
            yield Request(url=url, callback=self.parse, meta={'useSelenium': True, 'dont_redirect': True})
    def parse(self, response):
        content = WeiboItem()
        pictures = response.xpath("//*[@id='Pl_Official_MyProfileFeed__20']//li/img/@src").extract()
        x=0
        for pic in pictures:
            pic = "https:"+pic
            urllib.request.urlretrieve(pic, 'd:\\We\\%s.jpg' % x)
            x+=1
        content['content'] = "".join(response.xpath("//div[@class = 'WB_text W_f14']/text()").extract()).strip()

        yield content