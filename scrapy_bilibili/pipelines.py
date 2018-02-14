# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.utils.project import get_project_settings

class ScrapyBilibiliPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
    
    
    def get_media_requests(self, item, info):
        image_url = item['image_urls']
        yield scrapy.Request(image_url)
    
    
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item