#Hello world!
#Hello Git God, help me.
import json
import scrapy 

class CrawlerdolarSpider(scrapy.Spider):
    name = 'crawlerDolar'
    start_urls = ['https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwihztzp_oP7AhWXCLkGHVVkBlMQmY0JegQICRAb']

    def parse(self, response):
        value = response.xpath('//div[@class="YMlKec fxKbKc"]/text()').get()
        dolar = value[:4]
        print(value)
        print(dolar)

        with open("keywords.json", encoding='utf-8') as keywords:
            Data = json.load(keywords)
        
        if "dolar" in Data[-1]:
            print("Dólar está caríssimo.")

        with open("data.json", "w") as datafile:
            json.dump(dolar, datafile, indent=4, sort_keys=True, ensure_ascii=False)

