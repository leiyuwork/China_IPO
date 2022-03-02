import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os
i = 0
for code in range(301068, 301236):
    result = [code]
    url = "https://quotes.money.163.com/f10/gszl_" + str(code) + ".html"
    i = i + 1
    print("********" + str(code) + "処理中*************")
    time.sleep(3)
    try:
        dfs = pd.read_html(url)
        LotWin = dfs[4].iloc[8,1]
        TurnoverRate = dfs[4].iloc[14,1]
        result.append(LotWin)
        result.append(TurnoverRate)

    except Exception as e:
        print(e)
        result.append("null")
    final = pd.DataFrame([result])
    final.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\中签率首日换手率.csv",
                  mode="a",
                  index=False, header=None, encoding='utf_8_sig')

