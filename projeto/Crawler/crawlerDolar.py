import scrapy 

class CrawlerdolarSpider(scrapy.Spider):
    name = 'crawlerDolar'
    start_urls = ['https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwihztzp_oP7AhWXCLkGHVVkBlMQmY0JegQICRAb']

    def parse(self, response):
        value = response.xpath('//div[@class="kf1m0"]//text()').get()
        print(value)