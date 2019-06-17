import requests
from lxml import etree
import random
from urllib.parse import urlencode
from multiprocessing import Pool
from threading import Thread
from queue import Queue

from urllib import parse


headers={
    'Cookie':'SINAGLOBAL=6713963674280.896.1551149110607; UOR=www.google.com,www.weibo.com,www.baidu.com; un=15989260170; ULV=1556156545694:15:6:1:1418096230897.6897.1556156545675:1555549228901; wvr=6; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Whn64Ug1aFTy55.e-ehW56c5JpX5KMhUgL.Fo-RS0n01KMcSh22dJLoI7fDdcvadcvadcvadcv7; ALF=1587805486; SSOLoginState=1556269487; SCF=ArTrTFtoFUVAyWvJyEMo7ZgDpNG3Z-dV7ac0UEPK7QEWH2OhJmGdDu8sDYzD_YDppasiPGlyEi5narUBMHbrl28.; SUB=_2A25xxrn_DeRhGeNG7FoS-SnKzz2IHXVStaw3rDV8PUNbmtANLVDBkW9NSwsmFC8YOBHN9njDItMowKPLWbEs5QTS; SUHB=0mxUC3QLqcbg2R; YF-Page-G0=b9004652c3bb1711215bacc0d9b6f2b5|1556269488|1556269485',
    'Host':'d.weibo.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
url='https://d.weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=102803_ctg1_1760_-_ctg1_1760&pre_page=1&page=2&pids=Pl_Core_NewMixFeed__3&current_page=6&since_id=&pl_name=Pl_Core_NewMixFeed__3&id=102803_ctg1_1760_-_ctg1_1760&script_uri=/&feed_type=1&domain_op=102803_ctg1_1760_-_ctg1_1760&__rnd=1556157527759'
pp=requests.get(url,headers=headers)
#pp.encoding='utf-8'
oo=pp.text.encode("utf-8").decode("unicode_escape") #转码后的网页内容
