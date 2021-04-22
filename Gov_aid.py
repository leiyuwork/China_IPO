import requests
from bs4 import BeautifulSoup
import time
import os

headers = {
    'Accept': 'text/html, */*; q=0.01',
    'Referer': 'http://tv.cctv.com/lm/xwlb/',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'channelCode=3763BEXX; ylbcode=24S2AZ96; bdshare_firstime=1619108951840; JSESSIONID=aaaWdDw2JaELg46hCOlCx; WT_FPC=id=2ccc406d00ed3681a591619105350593:lv=1619105670570:ss=1619105350593'
}
for code in range(300001, 300002):
    print('*****************' + str(code) + '*****************')
    response = requests.get('http://stock.jrj.com.cn/share,' + str(code) + ',zgsms.shtml?to=pc', headers=headers)
    response.encoding = response.apparent_encoding
    bs_obj = BeautifulSoup(response.text, 'html.parser')

    linkSpan = bs_obj.find('ul', class_='newlist')

    response_2 = requests.get('http://stock.jrj.com.cn/' + linkSpan.find('a', href=True).attrs['href'], headers=headers)
    response_2.encoding = response.apparent_encoding
    bs_obj = BeautifulSoup(response_2.text, 'html.parser')
    print(bs_obj)


    """
    filename = os.path.join(r'C:\\Users\Ray94\Desktop\ipo', str(code)+'.pdf')
    with open(filename, 'wb') as f:
        f.write(requests.get("http:" + a.find('a', href=True).attrs['href']).content)
    """
