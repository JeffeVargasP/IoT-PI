#Hello world!
#Hello Git God, help me.
import json
import scrapy
dolar = {}

class dolarSpider(scrapy.Spider):
    name = 'crawlerDolar'
    start_urls = ['https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwihztzp_oP7AhWXCLkGHVVkBlMQmY0JegQICRAb']

    def parse(self, response):
        value = response.xpath('//div[@class="YMlKec fxKbKc"]/text()').get()
        dolar.append(value[:4])

        with open("keywords.json", encoding='utf-8') as keywords:
            Data = json.load(keywords)
        
        if "dolar" in Data[-1]:
            print("Dólar está caríssimo.")

        with open("data.json", "w") as datafile:
            json.dump(dolar, datafile, indent=4, sort_keys=True, ensure_ascii=False)