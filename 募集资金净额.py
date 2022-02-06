import pandas as pd  # データ解析を容易にする機能を提供する
import time
i = 0
for code in range(300001, 301000):
    url = "https://vip.stock.finance.sina.com.cn/corp/go.php/vISSUE_NewStock/stockid/" + str(code) + ".phtml"
    i = i + 1
    print("********" + str(i) + "社目処理中*************")
    time.sleep(3)

    dfs = pd.read_html(url)
    df = dfs[12][1].values.tolist()
    df.insert(0, str(code))
    print(df)
    Output = pd.DataFrame(df)
    Output.T.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\募集资金净额.csv",
                  mode="a",
                  index=False, header=None, encoding='utf_8_sig')



