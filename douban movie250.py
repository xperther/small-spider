import requests
from lxml import etree

title=[]
link=[]
count=[]
for i in range(10):
    url='https://movie.douban.com/top250?start=%d&filter='%(i*25)
    pp=requests.get(url)
    html=etree.HTML(pp.text)
    p=html.xpath("//div[@class='hd']/a/span[@class='title'][1]")
    h=html.xpath("//div[@class='hd']/a/@href")
    o=html.xpath("//div[@class='star']/span[@class='rating_num']")
    for i in range(len(p)):
        title.append(p[i].text)
        link.append(h[i])
        count.append(o[i].text)

