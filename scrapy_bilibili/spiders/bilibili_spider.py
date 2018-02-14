# -*- coding: utf-8 -*-
import json
import scrapy
from scrapy_bilibili.items import ScrapyBilibiliItem

class BilibiliSpider(scrapy.Spider):
    name = 'bilibili_spider'
    allowed_domains = ['api.vc.bilibili.com']
    page_num = 0
    start_urls = ['http://api.vc.bilibili.com/link_draw/v2/Doc/index?_device=android&_hwid=ATkKb1xoDjYDNQE2SnhKeEpzRXQSIxMlRjoLb15pD25XMnIQehR2QjBMdUAiUzJRIVNmH2oHfw&access_key=c9aa0568e3daae77e088993ed530b5d9&appkey=1d8b6e7d45233436&build=5220001&mobi_app=android&page_num=' + str(page_num) + '&page_size=20&platform=android&src=meizu&trace_id=20180213140300025&ts=1518501805&type=recommend&version=5.22.1.5220001&sign=7f898e656df0bf494f46a2d5474c1449']

    def parse(self, response):
        datas = json.loads(response.text)['data']['items']
        for data in datas:
            item = ScrapyBilibiliItem()
            for img in data['item']['pictures']:
                item['image_urls'] = img['img_src']
                yield item
        if self.page_num >= 10:
            return
        self.page_num += 1
        yield scrapy.Request('http://api.vc.bilibili.com/link_draw/v2/Doc/index?_device=android&_hwid=ATkKb1xoDjYDNQE2SnhKeEpzRXQSIxMlRjoLb15pD25XMnIQehR2QjBMdUAiUzJRIVNmH2oHfw&access_key=c9aa0568e3daae77e088993ed530b5d9&appkey=1d8b6e7d45233436&build=5220001&mobi_app=android&page_num=' + str(self.page_num) + '&page_size=20&platform=android&src=meizu&trace_id=20180213140300025&ts=1518501805&type=recommend&version=5.22.1.5220001&sign=7f898e656df0bf494f46a2d5474c1449', callback = self.parse)
