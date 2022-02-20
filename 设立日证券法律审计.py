import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os
i = 0
for code in range(300005, 301000):
    result = [code]
    url = "https://q.stock.sohu.com/cn/" + str(code) + "/gsjj.shtml"
    i = i + 1
    print("********" + str(i) + "社目処理中*************")
    time.sleep(3)
    try:
        dfs = pd.read_html(url)
        establishment = dfs[1].iloc[6,3]
        underwriter = dfs[2].iloc[5,1]
        audit = dfs[2].iloc[7,1]
        law = dfs[2].iloc[9,1]
        result.append(establishment)
        result.append(underwriter)
        result.append(audit)
        result.append(law)
    except:
        result.append("null")
    final = pd.DataFrame([result])
    final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\设立日证券法律审计.csv",
                  mode="a",
                  index=False, header=None, encoding='utf_8_sig')
