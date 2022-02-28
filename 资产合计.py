import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
df = pd.read_excel(r'C:\\Users\Ray94\Downloads\A股列表 (1).xlsx')


for code in range(300001, 301236):
    try:
        IPO = df.loc[df['A股代码'] == code, 'A股上市日期'].to_string(index=False).replace("-", "")
        url = "https://quote.cfi.cn/ItemHistory.aspx?table=a2zcfz&stockcode=" + str(code) + '&c=TotalAssets&column=%e8%b5%84%e4%ba%a7%e6%80%bb%e8%ae%a1&unit='
        print("********" + str(code) + "処理中*************")
        time.sleep(3)
        dfs = pd.read_html(url,encoding = "utf-8")[1]
        dfs.drop(dfs.head(2).index,inplace=True)
        dfs.drop(dfs.tail(1).index,inplace=True)
        dfs.insert(0, "Code", str(code))
        dfs[0].replace("-", "", inplace=True, regex=True)
        dfs[0] = dfs[0].astype(int)
        dfs.reset_index(drop=True, inplace=True)
        result = pd.DataFrame(dfs.iloc[dfs[dfs[0].le(int(IPO))].index[1]])
        result.T.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\资产总计.csv",
                             mode='a',
                             index=False, header=None,
                             encoding="utf-8_sig")
    except:
        pass


        
