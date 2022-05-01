from scrapy.settings import Settings
from fileparser import settings
from fileparser.spiders.leroymerlin import LeroymerlinSpider
from scrapy.crawler import CrawlerProcess

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider, search='жидкие+обои')
    process.start()
