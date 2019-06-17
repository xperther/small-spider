import sys
import time
import hashlib
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
_version = sys.version_info

is_python3 = (_version[0] == 3)

# 个人中心获取orderno与secret
orderno = "DT20190427124618LbQ2hRq2"    
secret = "a2de3eb6b9635c763cd0c57593939f06"

ip = "dynamic.xiongmaodaili.com"
port = "8088"

ip_port = ip + ":" + port
proxy = {"https": "https://" + ip_port}

def aa():
    timestamp = str(int(time.time()))                # 计算时间戳
    txt = ""
    txt = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp
    if is_python3:
        txt = txt.encode()
    md5_string = hashlib.md5(txt).hexdigest()                 # 计算sign
    sign = md5_string.upper()                              # 转换成大写
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
    headers = {"Proxy-Authorization": auth}
    return headers


basefont=requests.get(url,proxies=proxy,headers=aa(),verify=False,allow_redirects=False)
