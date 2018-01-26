# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from wiki.items import WikiItem

class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://de.wikipedia.org/wiki/Webcrawler']

    def createItem(self, response):
        item = WikiItem()
        soup = BeautifulSoup(response.extract(), 'html.parser')
        item['title'] = soup.h1.text
        item['content'] = soup.get_text()
        return item

    def parse(self, response):
        responseSelector = scrapy.Selector(response)
        for sectionId, section in enumerate(responseSelector.css('#content')):
            yield self.createItem(section)
