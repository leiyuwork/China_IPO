import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie':'ASP.NET_SessionId=etqt2dozlffvvnd0gypxy0og; 10600min54040010001101=false; quoteIsStart_cookiemin97035=; 97035min54040010001101=false; quoteIsStart_cookiemin10614=; 10614min54040010001101=false; quoteIsStart_cookiefund106001=; 106001fund54034010001101=false; quoteIsStart_cookiefund10699=; 10699fund54034010001101=false; quoteIsStart_cookiefund10698=; 10698fund54034010001101=false; quoteIsStart_cookiefund10649=; 10649fund54034010001101=false; quoteIsStart_cookiefund10628=; 10628fund54034010001101=false; history=his=300001%2c%e7%89%b9%e9%94%90%e5%be%b7%2ctrd%2c10600%7c300021%2c%e5%a4%a7%e7%a6%b9%e8%8a%82%e6%b0%b4%2cdyjs%2c10620%7c300027%2c%e5%8d%8e%e8%b0%8a%e5%85%84%e5%bc%9f%2chyxd%2c10626%7c162212%2c%e6%b3%b0%e8%be%be%e7%ba%a2%e5%88%a9%2ctdhl%2c10628%7c002302%2c%e8%a5%bf%e9%83%a8%e5%bb%ba%e8%ae%be%2cxbjs%2c10629%7c300022%2c%e5%90%89%e5%b3%b0%e7%a7%91%e6%8a%80%2cjfkj%2c10621%7c002305%2c%e5%8d%97%e5%9b%bd%e7%bd%ae%e4%b8%9a%2cngzy%2c10634%7c040015%2c%e5%8d%8e%e5%ae%89%e7%81%b5%e6%b4%bbA%2chalha%2c10649%7c002313%2c%e6%97%a5%e6%b5%b7%e6%99%ba%e8%83%bd%2crhzn%2c10656%7c; quoteIsStart_cookiemin10600=false'
}


for code in range(300001, 300586):
    print(code)
    try:
        result_00 = []
        result_plan = []
        result_date = []
        result_expenditure = []

        url_zbyz = "https://quote.cfi.cn/quote.aspx?actcontenttype=zbyz&searchcode=" + str(code)
        response = requests.get(url_zbyz, headers=headers)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        IPOdates = soup.find('table', id="tabh").find_all('tr')
        for IPOdat in IPOdates:
            dates = [ele.text.strip() for ele in IPOdat.find_all('td')]
            if (len(dates) > 3 and dates[1] == "首发新股"):
                IPOdate = int(dates[0].replace("-", ""))

        IPOprojects = soup.find_all('table', id="tabh")[1].find_all('tr')
        for project in IPOprojects[2::]:
            infos = project.find_all('td')
            cols = [ele.text.strip() for ele in infos]
            cols = [ele for ele in cols if int((cols[0]).replace("-", ""))<=IPOdate]
            if cols:
                cols.insert(0, code)
                result_00.append(cols) 
        result = pd.DataFrame(result_00)
        url_plan = "https://quote.cfi.cn/quote.aspx?actcontenttype=tzzk&searchcode=" + str(code) + "&jzrq=" + cols[1]
        response = requests.get(url_plan, headers=headers)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find("table", class_="vertical_table")
        for plan in table.find_all('tr')[5].find_all('td')[1::]:
            result_plan.append(plan.text)
        for plan in table.find_all('tr')[6].find_all('td')[1::]:
            result_date.append(plan.text)
        for plan in table.find_all('tr')[7].find_all('td')[1::]:
            result_expenditure.append(plan.text)
        Output = pd.DataFrame([result_plan,result_date,result_expenditure])
        Output = Output.T
        final = pd.concat([result, Output], axis=1)
        final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\planning20211228.csv", mode='a', index=False, header=None,encoding="utf-8_sig")
        time.sleep(3)
    except Exception as e:
        final= pd.DataFrame([[code,e]])
        final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\planning20211228.csv", mode='a', index=False, header=None,encoding="utf-8_sig")
        time.sleep(3)
