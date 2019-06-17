import requests
from lxml import etree
#from multiprocessing import Pool
from threading import Thread
#import concurrent.futures
#import time
import re
import urllib3
import random
from queue import Queue
from ip import Ip   #自己写的ip代理池


class Taobao():
    def __init__(self):
        self.s=requests.Session() #使用Session保持会话连接
        self.baseurl='https://www.taobao.com/'
        self.url='https://s.taobao.com/search?'
        self.page_url=''
        self.title=[]  #商品标题
        self.detail_url=[] #商品详情页
        self.price=[] #商品价格
        self.view_sales=[] #商品购买人数
        self.comment_count=[] #商品评论人数
        sefl.nick=[] #商品店铺
        self.pipe=Queue()
        self.ip=Ip() #初始化ip 获得ip代理池
        self.proxies={
            'https':random.choice(self.ip),
            }
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Cookie': #自己登陆后的cookie
            }
        

    def get_page(selfq,):
        p=self.s.get(self.baseurl,headers=self.headers,proxies=self.proxies)
        h=etree.HTML(p.text)
        l=h.xpath("//meta[@name='spm-id']/@content")[0] #获取data表单的spm值,不过好像这个spm是个定值，所以没必要获取？
        q=input('请输入你要查询的商品:')
        for i in range(100):
            data={
                'q':q ,
                'imgfile':'',
                'commend':'all',
                'ssid':'s5-e',
                'search_type':'item',
                'sourceId':'tb.index',
                'spm':l+'.2017.201856-taobao-item.1',
                'ie':'utf8',
                'initiative_id':'tbindexz_20170306',
                'bcoffset':'4',
                'p4ppushleft':'1%2C48',
                'ntoffset':'4',
                's':str(i*44)
                }
            url=self.url+urlencode(data)
            self.pipe.put(url)


            
    def get_data(self):
        while not pipe.empty():
            url=pipe.get()
            pp=self.s.get(url,headers=self.headers,proxies=self.proxies)
            hh=etree.HTML(pp.text)#使用正则表达式匹配网页中用js传递的值
            self.title=re.findall(r'"raw_title":"(.*?)"',hh.text)
            self.price=re.findall(r'"view_price":"(.*?)"',hh.text)
            self.view_sales=re.find(r'"view_sales":"(.*?)"',hh.text)
            self.comment_count=re.findall(r'"comment_count":"(.*?)"',hh.text)
            self.nick=re.findall(r'"nick":"(.*?)"',hh.text)
            a=re.findall(r'"detail_url":"(.*?)"',hh.text)#匹配到\u003d,\u0026的需要替
            for i in a:
                b=i.replace('\\u003d','=')
                c=b.replace('\\u0026','&')
                self.datail_url(c[2:])      
        
        
        
    def save(self):
        pass



if __name__ == '__main__':
    a=Taobao()
    a.get_page()
    b=[]
    for i in range(10):
        thread=Thread(target=a.get_data)
        thread.start()
        b.append(thread)

    for i in b:
        i.join()
    
        
    




























    
