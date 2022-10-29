import json
import urllib.request
import urllib
import scrapy

results = ["Dólar está 5 reais", "Dólar está 500 reais"]

with open("words.json", encoding='utf-8') as keywords:
    Data = json.load(keywords)

with open("data.json", "w") as datafile:
    json.dump(results, datafile, indent=4, sort_keys=True, ensure_ascii=False)

if "Dólar" in Data[-1]:
    print("Dólar está caríssimo.")


class dolarSpider(scrapy.Spider):
    name = "dolarSpider"
    url = "https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwihztzp_oP7AhWXCLkGHVVkBlMQmY0JegQICRAb"
    dado = urllib.request.xpath("//div[@class='quote']")