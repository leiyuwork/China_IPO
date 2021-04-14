import requests
from bs4 import BeautifulSoup
import time
import os

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'http://tv.cctv.com/lm/xwlb/',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
for code in range(300001, 300586):
    print('*****************' + str(code) + '*****************')
    response_1 = requests.get('http://stock.jrj.com.cn/share,' + str(code) +',zgsms.shtml?to=pc', headers=headers)
    time.sleep(5)
    response_1.encoding = 'gb18030'
    bs_obj = BeautifulSoup(response_1.text, 'lxml')
    linkSpan = bs_obj.find_all('ul', {'class': 'newlist'})
    for a in linkSpan:
        response_2 = requests.get("http://stock.jrj.com.cn/" + a.find('a', href=True).attrs['href'])
        response_2.encoding = 'gb18030'
        soup = BeautifulSoup(response_2.text, 'lxml')
        Span = soup.select('body > div.body > div.warp > div.main > table > tbody > tr > td.m > div.tabs2.txt > p.tc')
        for s in Span:
            filename = os.path.join(r'C:\Users\Ray94\Desktop\ipo', str(code)+'.pdf')
            with open(filename, 'wb') as f:
                f.write(requests.get(s.find('a', href=True).attrs['href']).content)

