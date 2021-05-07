import json
import urllib

import scrapy
import urllib3

from ..items import PvpSpiderItem


class PvpSpider(scrapy.Spider):
    name = 'pvp_spider'
    allowed_domains = ['pvp.qq.com']
    custom_settings = {
        'ITEM_PIPELINES': {'tutorial.pipelines.PvpPipeline': 302}
    }
    start_urls = [
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=1',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=2',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=3',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=4',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=5',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=6',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=7',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=8',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=9',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=10',
        'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&iListNum=60&iActId=2735&page=11']

    def parse(self, response):
        img_urls = json.loads(response.text)
        img_list = img_urls['List']
        p_item = PvpSpiderItem()
        for url in img_list:
            p_item['name'] = urllib.parse.unquote(url['sProdName'])
            # 获取url中 \ 出现的最后位置
            end = urllib.parse.unquote(url['sProdImgNo_6']).rfind('/')
            p_item['url'] = urllib.parse.unquote(url['sProdImgNo_6'])[0:end+1] + '0'
            yield p_item
