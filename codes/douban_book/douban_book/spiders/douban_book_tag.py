import scrapy


class DoubanBookTagSpider(scrapy.Spider):
    name = 'douban_book_tag'
    start_urls = [
        'https://book.douban.com/tag/?view=cloud',
    ]
    headers = {}

    def parse(self, response):
        trs = response.xpath('//table[@class="tagCol"]/tbody/tr')
        for tr in trs:
            tds = tr.xpath('td')
            for td in tds:
                title = td.xpath('a').pop().css('::text').get()
                href = 'https://book.douban.com' + td.xpath('a').pop().attrib.get('href', '')
                count = td.xpath('b').pop().css('::text').get().replace('(', '').replace(')', '')
                yield {'title': title, 'href': href, 'count': count}
