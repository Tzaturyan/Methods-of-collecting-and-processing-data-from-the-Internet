import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem


class SuperjobSpider(scrapy.Spider):
    name = 'superjob'
    allowed_domains = ['superjob.ru']
    start_urls = ['https://russia.superjob.ru/vacancy/search/?keywords=Data%20Science']

    def parse(self, response: HtmlResponse):
        links = response.xpath('//span[@class="_1e6dO _1XzYb _2EZcW"]/a/@href').getall()

        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)

    @staticmethod
    def vacancy_parse(response: HtmlResponse):
        name = response.xpath('//h1//text()').get()
        salary = response.xpath("//span[@class='_2Wp8I _1e6dO _1XzYb _3Jn4o']//text()")
        if salary:
            salary = salary.getall()
        link = response.url
        item = JobparserItem(name=name, salary=salary, link=link)
        yield item
