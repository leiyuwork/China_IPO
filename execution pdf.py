import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os
import re
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
from selenium import webdriver
options = webdriver.FirefoxOptions()
#options.set_headless(True)
options.add_argument("--headless") #设置火狐为headless无界面模式
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'cowCookie=true; qgqp_b_id=bf0ee593f5991050cc89d07c714f60ba; intellpositionL=636.797px; intellpositionT=2824px; has_jump_to_web=1'
   }

for code in range(300010, 301235):
    print(code)
    try:
        for number in range(1,55):
            url_door = "https://np-anotice-stock.eastmoney.com/api/security/ann?cb=jQuery112307762755490847939_1650607191961&sr=-1&page_size=50&page_index=" +  str(number) + "&ann_type=A&client_source=web&stock_list=" + str(code) 
            response = requests.get(url_door, headers=headers)
            s = re.findall(r'\{"art_code".*?\"title_en":""}', response.text)
            matches = ["募集资金", "使用情况", "鉴证报告"]
            for each in s:
                if all(x in each for x in matches):
                    for url_number in re.findall(r'"art_code":"[A-Z]{2}[0-9]{18}',each):
                        url_next = "https://data.eastmoney.com/notices/detail/" + str(code) + "/"+ str(url_number.replace('"art_code":"', '')) +".html"
                        print(url_next)
                        response_next =  driver.get(url_next)
                        html = driver.page_source.encode('utf-8')
                        soup = BeautifulSoup(html, "html.parser")
                        pdf_name = soup.find('div',{"class": "title_box"}).find('span', class_= 'title_text')
                        pdf_name=re.sub(r'[\':\s ,]*', '', pdf_name.text)
                        print(pdf_name)
                        pdf_url= soup.find('div',{"class": "title_box"}).find('a', href=True).attrs['href']
                        print(pdf_url)
                        filename = os.path.join(r'C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\plan-execution\\', str(code) + "  " + pdf_name + soup.find('span',{"id": "ggdate"}).text + '.pdf')
                        with open(filename, 'wb') as f:
                            f.write(requests.get(str(pdf_url)).content)
    except Exception as e:
        print(e)
        pass
