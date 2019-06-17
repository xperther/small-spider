import requests
from bs4 import BeautifulSoup
import json
import urllib3
import re
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class A():
    def __init__(self):
        self.title=[]
        self.link=[]
        self.nums=0

        
    def a(self,url):
        pp=requests.get(url,verify=False)
        pp.encoding = 'utf-8'
        bf=BeautifulSoup(pp.text)
        content=bf.find_all('div',id='article',class_='article')
        oo=content[0].text
        return oo

    def b(self):
        url='https://news.sina.com.cn'
        pp=requests.get(url,verify=False)
        pp.encoding='utf-8'
        bf=BeautifulSoup(pp.text)
        k=bf.find_all('div',class_='ct_t_01')
        i=BeautifulSoup(str(k[0]))
        m=i.find_all('a')
        self.nums=len(m)
        for n in m:
            self.title.append(n.string)     
            self.link.append(n.get('href'))

    def c(self,a,b,c):
        with open('text.txt','a',encoding='utf-8') as f:
            f.write(a)
            f.write(b)
            f.write(c)

            
if __name__=="__main__":
    z=A()
    z.b()
    
    for i in range(z.nums):
        z.c(z.title[i],z.a(z.link[i]),str(i))

        
    
        
    
    
