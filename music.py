import requests
from lxml import etree
import random
from urllib.parse import urlencode
from multiprocessing import Pool
from threading import Thread
from queue import Queue
from xiciip import Ip


class Music():
    def __init__(self):
        self.ip=Ip.ip()
        self.proxies={
            'https':'https'+random.choice(self.ip),
            }
        self.pipe=Queue
        self.name=[]
        self.song=[]
        self.a={}
        



    def start_requests(self):
        a=['1001','1002','1003','2001','2002','2003','6001','6002','6003','7001','7002','7003','4001','4002','4003']
        b=['0','65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90']
        for i in a:
            for j in b:
                url='https://music.163.com/discover/artist/cat?id={}&initial={}'.format(i,j)
                self.pipe.put(url)
        
            
        
    def parse(self, response):
        while not pipe.empty():
            url=pipe.get()
            pp=requests.get(url)
            pp=response.xpath("//li[@class='sml']/a/text()")
            for i in pp:
                item['name']=i
                yield ite
                urls=response.xpath("//li[@class='sml']/a/@href").extract()
                for i in urls:
                    url=baseurl+i
                    yield scrapy.Request(url,callback=self.get_song,meta=item)


    def get_song(self,response):
        item=MusicItem()
        pp=response.xpath("//ul[@class='f-hide']/li/a/text()").extract()
        item['song']=pp
        yield item



