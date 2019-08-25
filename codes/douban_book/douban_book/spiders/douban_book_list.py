# -*- coding: utf-8 -*-
import scrapy

from douban_book.items import DoubanBookItem

tags = ["小说", "历史", "日本", "外国文学", "文学", "中国", "心理学", "漫画", "哲学", "随笔", "中国文学", "经典",
        "推理", "爱情", "美国", "日本文学", "绘本", "传记", "社会学", "文化", "散文", "青春", "成长", "科普", "英国",
        "东野圭吾", "生活", "科幻", "悬疑", "旅行", "艺术", "言情", "思维", "社会", "心理", "经济学", "管理", "村上春树",
        "法国", "励志", "设计", "政治", "台湾", "人生", "女性", "经济", "好书，值得一读", "诗歌", "奇幻", "商业", "人性",
        "武侠", "推理小说", "童话", "摄影", "日本漫画", "英国文学", "金融", "美国文学", "建筑", "宗教", "儿童文学", "名著",
        "耽美", "古典文学", "电影", "政治学", "计算机", "投资", "韩寒", "互联网", "教育", "个人管理", "我想读这本书", "数学",
        "王小波", "余华", "网络小说", "亦舒", "杂文", "人类学", "职场", "三毛", "治愈", "中国历史", "東野圭吾", "纪实",
        "美食", "科幻小说", "张爱玲", "工具书", "回忆录", "香港", "当代文学", "德国", "温暖", "日系推理", "思想",
        "阿加莎·克里斯蒂", "散文随笔", "营销", "法国文学", "编程", "安妮宝贝", "金庸", "游记", "国学", "英语", "科学",
        "教材", "穿越", "自我管理", "刘慈欣", "政治哲学", "心灵", "时间管理", "英文原版", "郭敬明", "毛姆", "人物传记"]
start_urls = [f'https://book.douban.com/tag/{i}' for i in tags]


class DoubanBookListSpider(scrapy.Spider):
    name = 'douban_book_list'
    allowed_domains = ['book.douban.com']
    start_urls = start_urls

    def parse(self, response):
        lis = response.xpath('//ul[@class="subject-list"]/li')
        for li in lis:
            img = li.xpath('div[1]/a/img').attrib.get('src', '')
            info_attr = li.xpath('div[2]/h2/a').attrib
            href = info_attr.get('href', '')
            title = info_attr.get('title', '')
            about = li.xpath('div[2]/div').css('::text').get().strip()
            rate = li.xpath('div[2]/div[2]/span[2]').css('::text').get()
            rate_count = li.xpath('div[2]/div[2]/span[3]').css('::text').get().strip()
            desc = li.xpath('div[2]/p').css('::text').get()

            body = {
                'img': img,
                'href': href,
                'title': title,
                'about': about,
                'rate': rate,
                'rate_count': rate_count,
                'desc': desc,
            }
            item = DoubanBookItem()
            for k, v in body.items():
                item[k] = v
            yield item

        next = response.xpath('//span[@class="next"]/a').attrib.get('href', '')
        if next:
            next = f'https://book.douban.com{next}'
            yield scrapy.Request(next, callback=self.parse)
