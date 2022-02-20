import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os
options = webdriver.FirefoxOptions()
#options.set_headless(True)
options.add_argument("--headless") #设置火狐为headless无界面模式
options.add_argument("--disable-gpu")
driver = webdriver.Firefox(options=options)

i = 0
for code in range(300756, 301000):
    result = [code]
    driver.get("https://basic.10jqka.com.cn/" + str(code) + "/capital.html")
    i = i + 1
    print("********" + str(code) + "処理中*************")
    time.sleep(3)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    try:
        dfs = pd.read_html(html,encoding='utf-8')
        #print(dfs[1])
        if '项目简介' in dfs[1].columns:
            try:
                a = dfs[1].loc[(dfs[1]['承诺使用募集资金(元)']=='-') & (dfs[1]['已投入募集资金(元)']=='-')& (dfs[1]['建设期(年)']=='-')& (dfs[1]['税后收益率']=='-')& (dfs[1]['预测年新增净利润(元)']=='-')& (dfs[1]['项目简介']=='-')].values.tolist()[0]
                result.append(a)
            except:
                result.append("NULL")
        else:
            result.append("NULL")
        final = pd.DataFrame([result])
        final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\判断营运资金.csv", mode='a', index=False,header=None,
                      encoding="utf-8_sig")
        time.sleep(3)
    except:
        result.append("NULL")
        final = pd.DataFrame([result])
        final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\判断营运资金.csv", mode='a', index=False,header=None,
                      encoding="utf-8_sig")
        time.sleep(3)
        
