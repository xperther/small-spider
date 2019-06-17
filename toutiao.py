import requests
from bs4 import BeautifulSoup
import json
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

'''
#获取24小时新闻的 URL tiile
url='https://www.toutiao.com/api/pc/realtime_news/'
pp=requests.get(url)
data=json.loads(pp.text)
news=data['data']
l='https://www.toutiao.com'
for i in news:
    title=i['title']
    #group_id=i['article_url']
    url=i['open_url'].replace('group/','a')
    print(l+url,title)
'''

#获取新闻内容
url='https://www.toutiao.com/a6668131472643195400/'
pp=requests.get(url)
o=BeautifulSoup(pp.text,'lxml')
title=o.select('title')[0].get_text()
i=re.compile('content:\s*\'(.*?)\'')
v=re.search(i,pp.text).group()
print(v)


