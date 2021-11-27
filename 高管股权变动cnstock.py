import pandas as pd  # データ解析を容易にする機能を提供する
import time
i = 0
for code in range(300001, 300600):
    url = "http://data.cnstock.com/gpsj/ggcg/" + str(code) + ".html"
    i = i + 1
    print("********" + str(i) + "社目処理中*************")
    try:
        dfs = pd.read_html(url)
        dfs[0].insert(0, "Code", str(code))
        dfs[0].to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\china_GEM_TMTshareholder_log.csv", mode='a',
                           index=False, header=None, encoding="utf-8_sig")
        time.sleep(3)

    except Exception as e:
        Error = pd.DataFrame([[str(code), str(e)]])
        print(str(code) + " ERROR 発生" + Error)
        Error.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\IPO\china_GEM_TMTshareholder_error.csv",
                     mode='a',
                     index=False, header=None,
                     encoding="utf-8_sig")
        pass