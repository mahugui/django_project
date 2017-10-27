import re
import json
from urlparse import urlparse
import urllib
import pdb


from scrapy.selector import Selector
try:
    from scrapy.spiders import Spider
except:
    from scrapy.spiders import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor as sle

from v2ex_app.models import DataItem
from misc.log import *
from misc.spider import CommonSpider


class v2exSpider(CommonSpider):
    name = "v2ex"
    allowed_domains = ["v2ex.com"]
    start_urls = [
        "https://www.v2ex.com/",
    ]
    rules = [
        Rule(sle(allow=("https://www.v2ex.com/$")), callback='parse_1', follow=True),
    ]

    list_css_rules = {
        '.cell.item': {
            'title': '.item_title a::text',
            'node': '.node::text',
            'author': '.node+ strong a::text',
            'reply_count': '.count_livid::text',
            'url': '.item_title a::attr(href)'
        }
    }

    def parse_1(self, response):
        print(response)
        info('Parse '+response.url)

        # import pdb; pdb.set_trace()

        x = self.parse_with_rules(response, self.list_css_rules, dict)

        for cell_item in x[0]['.cell.item']:

            item = DataItem()
            item["title"] = cell_item["title"][0] if cell_item["title"] else ""
            item["node"] = cell_item["node"][0] if cell_item["node"] else ""
            item["reply_count"] = cell_item["reply_count"][0] if cell_item["reply_count"] else ""
            item["url"] = cell_item["url"][0] if cell_item["url"] else ""
            item["author"] = cell_item["author"][0] if cell_item["author"] else ""
            item["name"] = self.name
            item["base_url"] = self.start_urls[0]
            yield item
        # item["name"] = json.dumps(x, ensure_ascii=False, indent=2)
        # return item
        #pp.pprint(x)
        # return self.parse_with_rules(response, self.css_rules, v2exItem)


