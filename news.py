import os,django
os.environ['DJANGO_SETTINGS_MODULE'] = 'blogproject.settings'
django.setup()
from News.models import Post
import requests
from lxml import etree

class New():
    def __init__(self):
        self.title=[]
        self.urls=[]
        self.content=[]
        self.create_data=[]

    def get_urls(self): #获取新闻标题和新闻详情页的url
        url='https://news.163.com/'
        html=requests.get(url)
        a=etree.HTML(html.text)
        b=a.xpath("//div[@class='mod_top_news2']/h2")
        for i in b:
            self.title.append(i.xpath(".//a/text()")[0])
            self.urls.append(i.xpath(".//a/@href")[0])
        c=a.xpath("//div[@class='mod_top_news2']/ul/li")
        for i in c:
            j=i.xpath("./a")
            for h in j:
                self.title.append(h.xpath(".//text()")[0])
                self.urls.append(h.xpath(".//@href")[0])

    def get_content(self): #获取新闻的正文内容和发布时间
        for i in self.urls:
            a=''
            html=requests.get(i)
            b=etree.HTML(html.text)
            c=b.xpath("//div[@class='post_time_source']/text()")
            self.create_data.append(c[0].split()[0]+' '+c[0].split()[1])
            d=b.xpath("//div[@class='post_text']/p")
            for i in d:
                if i.xpath("./text()"):
                    a+='\n    '+i.xpath("./text()")[0]
                else:
                    pass
            self.content.append(a)

if __name__=='__main__':
    a=New()
    a.get_urls()
    a.get_content()
    for i in range(len(title)):
        add=Post(title=a.title[i],link=a.urls[i],body=a.content[i],
                 create_data=a.create_data[i])
        add.save()
