import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}

for code in range(300001, 301236):
    try:
        url = "https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/" + str(code) + ".phtml"
        
        dfszhaogu = pd.read_html(url)
        dfzhaogu = dfszhaogu[12][1].values.tolist()
        IPO = dfzhaogu[-2].replace("-", "")
        
        url_fuzhai = "https://quote.cfi.cn/ItemHistory.aspx?table=a2zcfz&stockcode=" + str(code) + '&c=TotalLiability&column=%e8%b4%9f%e5%80%ba%e5%90%88%e8%ae%a1&unit='
        print("********" + str(code) + "负债処理中*************")
        
        dfs_fuzhai = pd.read_html(url_fuzhai,encoding = "utf-8")[1]
        dfs_fuzhai.drop(dfs_fuzhai.head(2).index,inplace=True)
        dfs_fuzhai.drop(dfs_fuzhai.tail(1).index,inplace=True)
        dfs_fuzhai.insert(0, "Code", str(code))
        dfs_fuzhai[0].replace("-", "", inplace=True, regex=True)
        dfs_fuzhai[0] = dfs_fuzhai[0].astype(int)
        dfs_fuzhai.reset_index(drop=True, inplace=True)
        result_fuzhai = pd.DataFrame(dfs_fuzhai.iloc[dfs_fuzhai[dfs_fuzhai[0].le(int(IPO))].index[0]])
        result_fuzhai.T.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\负债合计.csv",
                             mode='a',
                             index=False, header=None,
                             encoding="utf-8_sig")
        time.sleep(5)
        
        url_zichan = "https://quote.cfi.cn/ItemHistory.aspx?table=a2zcfz&stockcode=" + str(code) + '&c=TotalAssets&column=%E8%B5%84%E4%BA%A7%E6%80%BB%E8%AE%A1&unit='
        print("********" + str(code) + "资产処理中*************")
        
        dfs_zichan = pd.read_html(url_zichan,encoding = "utf-8")[1]
        dfs_zichan.drop(dfs_zichan.head(2).index,inplace=True)
        dfs_zichan.drop(dfs_zichan.tail(1).index,inplace=True)
        dfs_zichan.insert(0, "Code", str(code))
        dfs_zichan[0].replace("-", "", inplace=True, regex=True)
        dfs_zichan[0] = dfs_zichan[0].astype(int)
        dfs_zichan.reset_index(drop=True, inplace=True)
        result_zichan = pd.DataFrame(dfs_zichan.iloc[dfs_zichan[dfs_zichan[0].le(int(IPO))].index[0]])
        result_zichan.T.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\资产合计.csv",
                             mode='a',
                             index=False, header=None,
                             encoding="utf-8_sig")
        time.sleep(5)
    except Exception as e:
        print(e)
        pass


        
