import time  # 時刻に関するさまざまな関数を使用するためのパッケージ
import pandas as pd  # データ解析を容易にする機能を提供する
import requests  # WEBスクレイピングでHTMLファイルからデータを取得するのに使われる
from bs4 import BeautifulSoup  # 取得したHTMLファイルをさらに解析するライブラリ
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

for code in range(300001, 300002):
    try:
        result = []
        url_door = "https://quote.cfi.cn/" + str(code) + ".html"
        response = requests.get(url_door, headers=headers)
        response.encoding = response.apparent_encoding
        soup = BeautifulSoup(response.text, 'html.parser')
        number = str(
            soup.find('div', {"id": "nodea22"}).find('a')['href'].replace(str(code), "").replace(".html", "").replace(
                "ggcgbd", "").replace("/", ""))
        url_mng_share = "https://quote.cfi.cn/ggcgbd/" + str(number) + "/" + str(code) + ".html"
        dfs = pd.read_html(url_mng_share)
        dfs[4].dropna(how='all', inplace=True)
        dfs[4].dropna(axis=1, how='all', inplace=True)
        df_list = dfs[4].tail(dfs[4].shape[0] - 2).values.tolist()
        for item in df_list:
            item.insert(0, str(code))
            result.append(item)
        time.sleep(1)
        print("***********************" + str(code) + "  書き込み開始" + "***********************")
        Output = pd.DataFrame(result)
        Output.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\china_GEM_TMT_sharechange_data.csv",
                      mode="a",
                      index=False, header=None, encoding='utf_8_sig')
        log = pd.DataFrame([[str(code)]])

        log.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\china_GEM_TMT_sharechange_log.csv",
                   mode='a',
                   index=False, header=None, encoding="utf-8_sig")
    except Exception as e:
        Error = pd.DataFrame([[str(code), str(url_mng_share), str(e)]])
        print(str(code) + " ERROR 発生" + Error)
        Error.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\china_GEM_TMT_sharechange_error.csv",
                     mode='a',
                     index=False, header=None,
                     encoding="utf-8_sig")
        pass