from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from mycrawler.spiders.broken_link import BrokenLinkSpider


process = CrawlerProcess(get_project_settings())
process.crawl(BrokenLinkSpider)
process.start()
