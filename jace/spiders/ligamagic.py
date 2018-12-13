# -*- coding: utf-8 -*-
import scrapy

from jace.commons import error_handling
from jace.commons.parsers.baseparser import Parser

HEADERS = {
    'authority': 'www.ligamagic.com.br',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
}


class LigamagicSpider(scrapy.Spider):
    name = 'ligamagic'

    def __init__(self, card=None, *args, **kwargs):
        super(LigamagicSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.ligamagic.com.br/?view=cards/search&card={card}']
        self.card = card

    # comment because setting default in settings.py
    # custom_settings = {
    #     'ROBOTSTXT_OBEY': False,
    # }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                method="GET",
                headers=HEADERS,
                callback=self._on_request_result,
                errback=error_handling.on_error,
                dont_filter=True
            )

    def _on_request_result(self, response):
        self.logger.info('_on_request_result')
        if response.status == 200:
            raw_parser = Parser(name=self.name, body=response.body, card=self.card)
            parser = raw_parser.call_correct_file(self.name)
            print(parser.soup)



