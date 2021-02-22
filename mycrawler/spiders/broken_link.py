from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mycrawler.items import BrokenLink


class BrokenLinkSpider(CrawlSpider):
    handle_httpstatus_list = [400, 403, 404, 500, 502, 503, 504]
    name = 'broken_link_spider'
    # Replace the value with the real domain.
    allowed_domains = ['crawler-test.com']
    # Replace the value with the website URL to crawl from.
    start_urls = ['https://crawler-test.com/links/broken_links_internal']
    custom_settings = {
        'LOG_FILE': 'logs/newNewNOINDEX.log',
        'LOG_LEVEL': 'INFO'
    }

    rules = (
        Rule(
            LinkExtractor(
                tags='a',
                attrs='href',
                unique=True,
            ),
            callback='parse_item',
            follow=True,

        ),
    )

    def parse_item(self, response):
        item = BrokenLink()
        item['title'] = response.css('title::text').extract_first()
        item['curr_url'] = response.request.url
        item['dest_url'] = response.url
        item['status'] = response.status
        item['text'] = response.meta['link_text']
        print(item)
        return item
