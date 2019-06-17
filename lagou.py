import requests
from lxml import etree
import random
from urllib.parse import urlencode
from multiprocessing import Pool
from threading import Thread
from queue import Queue
from urllib import parse #用来转码中文，因为headers不能有中文
import csv


class Lagou():
    def __init__(self):
        #使用Session()方法来传递cookies所以不需要设置cookies

        self.url=[]
        self.s=requests.Session()
        self.title=[] #岗位
        self.salary=[] #薪酬
        self.city=[] #城市
        self.company=[] #公司
        self.workyear=[] #工作经历
        self.positionAdvantage=[] #岗位优点
        self.id=[]
        self.f=''
        self.p=''
        self.pipe=Queue()
        self.page_num=0



    def get_id(self):
        self.s=requests.Session()
        if self.p == '':
            self.p=input('查询的岗位:')
        self.f=parse.quote(self.p)
         #这里我搜索的城市是广州，如果想换地方的话urls的city改成城市名
        #注意这里如果用%s船值，会于city的值有所冲突，%E%B等等
        a='https://www.lagou.com/jobs/list_{}?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='.format(self.f)
        
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Referer':'https://www.lagou.com/',
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token':'None',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'www.lagou.com',
            }
        p=self.s.get(a,headers=headers)
        

    def get_data(self):
        
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Referer':'https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput='.format(self.f),
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token':'None',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'www.lagou.com',
            }
        

        urls='https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
        
         #这一部分先获取总数据的数量再计算页数
        dataa={
            'frist':'false',
            'pn':'1',
            'kd':self.p,
            }
        pp_nums=self.s.post(urls,data=dataa,headers=headers)

        aosd=pp_nums.json()
        totalcount=aosd['content']['positionResult']['totalCount']  #拿到总数量
        print("共有%d个岗位"%totalcount)
        self.page_num=(totalcount//15)+1#总页数 ，一页15个数据


        
        for i in range(1,self.page_num+1):#这里可以使用多线程跑，节省时间。具体的创建一个管道，分别加入url
            data={
                'frist':'false',
                'pn':i,
                'kd':self.p
                }
            try:
                pp=self.s.post(urls,data=data,headers=headers)
                a=pp.json()
                c=a['content']['hrInfoMap']
                self.id=c.keys()
                b=a['content']['positionResult']['result']
                for i in b:
                    self.title.append(i['positionName'])
                    self.salary.append(i['salary'])
                    self.city.append(i['city'])
                    self.company.append(i['companyFullName'])
                    self.workyear.append(i['workYear'])
                    self.positionAdvantage.append(i['positionAdvantage'])
                print("第%d页"%data['pn'])
            except:
                self.get_id()
                pp=self.s.post(urls,data=data,headers=headers)
                a=pp.json()
                c=a['content']['hrInfoMap']
                self.id=c.keys()
                b=a['content']['positionResult']['result']
                for i in b:
                    self.title.append(i['positionName'])
                    self.salary.append(i['salary'])
                    self.city.append(i['city'])
                    self.company.append(i['companyFullName'])
                    self.workyear.append(i['workYear'])
                    self.positionAdvantage.append(i['positionAdvantage'])
                print("第%d页"%data['pn'])

        def save(self):
            with open('citylist.csv','a',newline='') as fp:
                writer = csv.writer(fp)
                writer.writerow(['岗位','工资','城市','公司','工作经历','岗位优点'])
                for i in range(len(self.title)):
                    writer.writerow([self.title[i],self.salary[i],self.city[i],self.company[i],self.workyear[i],
                              self.positionAdvantage[i]])

if __name__=='__main__':
    v=Lagou()
    v.get_id()
    v.get_data()
    #v.save()

#多线程
'''
import requests
from lxml import etree
import random
from urllib.parse import urlencode
from multiprocessing import Pool
from threading import Thread
from queue import Queue
from urllib import parse #用来转码中文，因为headers不能有中文
import time


class Lagou():
    def __init__(self):
        #使用Session()方法来传递cookies所以不需要设置cookies

        self.url=[]
        self.urlll=[]
        self.s=requests.Session()
        self.title=[] #岗位
        self.salary=[] #薪酬
        self.city=[] #城市
        self.company=[] #公司
        self.workyear=[] #工作经历
        self.positionAdvantage=[] #岗位优点
        self.urls=''
        self.f=''
        self.p=''
        self.pipe=Queue()
        self.page_num=0
        self.headers=[]


    def get_id(self):
        self.s=requests.Session()
        if self.f == '':
            self.p=input('查询的岗位:')
        self.f=parse.quote(self.p)
        #这里我搜索的城市是广州，如果想换地方的话urls的city改成城市名
        #注意这里如果用%s船值，会于city的值有所冲突，%E%B等等
        a='https://www.lagou.com/jobs/list_{}?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='.format(self.f)
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Referer':'https://www.lagou.com/',
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token':'None',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'www.lagou.com',
            }
        self.s.get(a,headers=headers)
        
 
    def get_data(self):

        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
            'Referer':'https://www.lagou.com/jobs/list_{}?labelWords=&fromSearch=true&suginput='.format(self.f),
            'X-Anit-Forge-Code':'0',
            'X-Anit-Forge-Token':'None',
            'X-Requested-With':'XMLHttpRequest',
            'Host':'www.lagou.com',
            }

        self.urls='https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
        
         #这一部分先获取总数据的数量再计算页数
        dataa={
            'frist':'false',
            'pn':'1',
            'kd':self.p,
            }
        pp_nums=self.s.post(self.urls,data=dataa,headers=self.headers)
        aosd=pp_nums.json()
        totalcount=aosd['content']['positionResult']['totalCount']  #拿到总数量
        print("共有%d个岗位"%totalcount)
        self.page_num=(totalcount//15)+1  #总页数 ，一页15个数据
        for i in range(1,self.page_num+1):#这里可以使用多线程跑，节省时间。具体的创建一个管道，分别加入url
            data={
                'frist':'false',
                'pn':i,
                'kd':self.p
                }
            self.pipe.put(data)
        
    def abc(self):#对于拉钩的cookies值好像只能访问9次数据，超过就需要重新获取cookies   
        while not self.pipe.empty():
            data=self.pipe.get()
            try:
                pp=self.s.post(self.urls,data=data,headers=self.headers)
                self.urlll.append('1')
                
                a=pp.json()
                b=a['content']['positionResult']['result']
                if b == []:
                    print("第%d页是空数据"%data['pn'])
                for i in b:
                    self.title.append(i['positionName'])
                    self.salary.append(i['salary'])
                    self.city.append(i['city'])
                    self.company.append(i['companyFullName'])
                    self.workyear.append(i['workYear'])
                    self.positionAdvantage.append(i['positionAdvantage'])
                print("第%d页"%data['pn'])
            except: 
                self.get_id()
                self.pipe.put(data)
                time.sleep(2)

if __name__=='__main__':
    v=Lagou()
    v.get_id()
    v.get_data()
    kk=[]
    for i in range(10):
        thread=Thread(target=v.abc)
        thread.start()
        kk.append(thread)

    for i  in kk:
        i.join()

'''
