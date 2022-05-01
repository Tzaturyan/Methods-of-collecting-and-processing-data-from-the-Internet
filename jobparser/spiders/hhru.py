import scrapy
from scrapy.http import HtmlResponse
from jobparser.items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = 'hhru'
    allowed_domains = ['hh.ru']
    start_urls = ['http://hh.ru/']
    search = 'Data+Science'

    start_urls = [f'https://hh.ru/search/vacancy?area=1&search_field=name&search_field=company_name&search_field=description&only_with_salary=true&text={search}&showClusters=true']

    def parse(self, response: HtmlResponse):
        next_page = response.xpath('//a[@data-qa="pager-next"]/@href').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        vacancy_links = response.xpath('//a[@data-qa ="vacancy-serp__vacancy-title"]/@href').getall()
        for link in vacancy_links:
            yield response.follow(link, callback=self.vacancy_parse)
        pass

    @staticmethod
    def vacancy_parse(self, response: HtmlResponse):
        name = response.xpath('//h1//text()').get()
        salary = response.xpath("//span[@class='bloko-header-section-3']//text()").extract_first().replace(u'\u202f', u'')

        link = response.url
        item = JobparserItem(name=name, salary=salary, link=link)
        yield item

        pass

