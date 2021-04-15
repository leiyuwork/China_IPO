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
for code in range(300219, 300586):
    print('*****************' + str(code) + '*****************')
    response = requests.get('https://data.eastmoney.com/xg/xg/detail/' + str(code) +'.html', headers=headers)
    time.sleep(3)
    bs_obj = BeautifulSoup(response.text, 'lxml')
    linkSpan = bs_obj.select('body > div.main > div:nth-child(12) > div > div.fr')
    print(linkSpan)
    for a in linkSpan:
        filename = os.path.join(r'C:\Users\Ray94\Desktop\ipo', str(code)+'.pdf')
        with open(filename, 'wb') as f:
            f.write(requests.get("http:" + a.find('a', href=True).attrs['href']).content)

