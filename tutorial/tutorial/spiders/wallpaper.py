import scrapy

from ..items import WallPaperItem


class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper'
    start_urls = ['http://quotes.toscrape.com/']
    custom_settings = {
        'ITEM_PIPELINES': {'tutorial.pipelines.WallPaperPipeline': 300}
    }

    def parse(self, response):
        div = response.xpath('//div[@class="quote"]')
        w = WallPaperItem()
        next_page = response.css('li.next a::attr(href)').get()
        for d in div:
            w['author'] = d.xpath('span/small/text()').get()
            w['text'] = d.css('span.text::text').get()
            w['tag'] = d.xpath('div//a/text()').getall()
            w['next_page'] = next_page
            yield w

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
