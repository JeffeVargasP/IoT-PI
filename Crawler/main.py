from scrapy.crawler import CrawlerProcess
from cdolar import dolarSpider

def execDolar():
    process = CrawlerProcess()
    process.crawl(dolarSpider)
    process.start()

execDolar()