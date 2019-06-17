from bs4 import BeautifulSoup
import requests, sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class downloader(object):
    def __init__(self):
        self.server = 'https://www.biqudu.com/'
        self.target = 'https://www.biqudu.com/43_43821/'
        self.names = []         #存放章节名
        self.urls = []          #存放章节链接
        self.nums = 0           #章节数

    def get_download_url(self):
        req = requests.get(url = self.target,verify=False)
        div_bf = BeautifulSoup(req.text)
        div = div_bf.find_all('div', id='list')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[12:])                             #剔除不必要的章节，并统计章节数
        for i in a[12:]:
            self.names.append(i.string)
            self.urls.append(self.server + i.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target,verify=False)
        bf = BeautifulSoup(req.text)
        texts = bf.find_all('div', id='content')
        texts = texts[0].text.replace('\u3000\u3000','\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《圣墟》开始下载：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '圣墟.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《圣墟》下载完成')

