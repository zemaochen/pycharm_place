# -*- coding: utf-8 -*-
import scrapy
from ..items import ItcastItem

class DemoSpider(scrapy.Spider):
    # 识别名称，必须是唯一的
    name = 'Demo'
    # 搜索的域名范围，也就是爬虫的约束区域
    allowed_domains = ['itcast.cn']
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml',
    ]
    def parse(self, response):
        # 爬取网页源码保存到teacher.html
        # filename = "teacher.html"
        # html = open(filename, 'wb+')
        # html.write(response.body)
        items = []
        # <div class="li_txt">
        #   <h3>吴老师</h3>
        #   <h4>高级讲师</h4>
        #   <p>有多年PHP开发和项目管理经验，开发过聊天在线系统、客户关系管理系统、智能SEM竞价系统等项目，精通PHP、mysql、linux、javascript、html5、css3等主流的web开发技术，讲课风格风趣幽默有激情，善于启发学生自我思考来解决问题。</p>
        # </div>
        for each in response.xpath("//div[@class='li_txt']"):
        # 将得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()
        # extract()方法返回的都是unicode字符串
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
        # xpath返回的是包含一个元素的列表
            item['name'] = name[0]
            item['level'] = title[0]
            item['info'] = info[0]
            items.append(item)
        # 直接返回最后数据
        return items
# scrapy startproject Demo
# scrapy crawl Demo
# scrapy crawl Demo -o teachers.csv




