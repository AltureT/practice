import scrapy
from practiceone.items import PracticeoneItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes=response.css('.quote')
        for quote in quotes:
            item = PracticeoneItem()
            item['text'] = quote.css('.text::text').extract_first()
            item['author'] = quote.css('.author::text').extract_first()
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        next=response.css('.pager .next a::attr("href")').extract_first()
        url=response.urljoin(next)
        yield scrapy.Request(url=url,callback=self.parse)
