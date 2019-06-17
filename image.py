import requests
import re
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class A():
    def __init__(self):
        self.name=[]
        self.link=[]
        self.download_url=[]
        
        
    #获取图片页数和页数URL  
    def getpage(self):
        j=input("输入你想下载的总页数（一页10张图片）:")
        for i in range(1,int(j)+1):
            p='https://unsplash.com/napi/photos?page=%d&per_page=10' %i
            self.link.append(p)

            
    #获取图片ID 和 下载地址URL
    def get_id_url(self):
        for j in range(len(self.link)):
            req=requests.get(url=self.link[j],verify=False)
            o=req.json()
            for i in o:
                self.name.append(i['id'])
                self.download_url.append(i['links']['download'])
               
    #保存图片
    def save_img(self):
        for i in range(len(self.download_url)):
            img=requests.get(url=self.download_url[i],verify=False)
            with open('%s.jpg' %self.name[i],'wb') as f:
                f.write(img.content)
            print('%s下载完成' %self.name[i])
        
            
if __name__=='__main__':
    w=A()
    w.getpage()
    w.get_id_url()
    w.save_img()

    
    

