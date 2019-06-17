import requests
from bs4 import BeautifulSoup
import urllib3
from urllib.parse import urlencode
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''
pp=requests.get('https://www.guokr.com/article/445989/')
html=etree.HTML(pp.text)
p=html.xpath("//div[@class='document']/div//text()")
tr=''
for i in range(len(p)):
    if  '\r\n' in p[i]:
       p[i]='\n'
       tr=tr+p[i]
    else:
        tr=tr+p[i]
with open('f.txt','a',encoding='utf-8') as f:
    f.write(tr)

'''

class A():
    def __init__(self):
        self.title=[]
        self.link=[]
        self.auth=[]
        self.num=''
        self.url='https://www.guokr.com/apis/minisite/article.json?'

    def get_url_title(self):
        self.num=input('请输入页数：（一页20篇文章）')
        for i in range(int(self.num)):
            offset=str(i*20)
            data={
                'retrieve_type': "by_subject",
                'limit': "20",
                'offset': offset,
                '_': '1552961543979',
                }
            pp=requests.get(self.url+urlencode(data))
            k=pp.json()
            g=k['result']
            for y in range(len(g)):
                self.title.append(g[y]['title'])
                self.auth.append(g[y]['author']['nickname'])
                self.link.append(g[y]['url'])
            

    def content(self,url):
        p=requests.get(url)
        p.encoding='utf-8'
        o=BeautifulSoup(p.text,'lxml')
        k=o.find_all('div',class_='document')
        n=BeautifulSoup(str(k[0]))
        j=n.find('div')
        return j.text

    def save_content(self,a,b):
        with open('p.txt','a',encoding='utf-8')as f:
            f.write(a)
            f.write(b)
            



if __name__=="__main__":
    a=A()
    a.get_url_title()
    for i in range(len(a.link)):
        a.save_content(a.title[i],a.content(a.link[i]))

            
        
