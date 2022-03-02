import pandas as pd  # データ解析を容易にする機能を提供する
import time
df = pd.read_excel(
    r'C:\\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\01.ChiNextTMT_300001-301235_20220225_EntityIdentification - 処理用.xlsx')
all_list = df.values.tolist()

new_df = df.drop(columns=["企業コード", "カテゴリー", "番号", "履歴"])

new_df.head()

all_newlist = new_df.values.tolist()

result = []
for lists in all_newlist:
    for values in lists:
        if not values in result:
            result.append(values)

Output = pd.DataFrame(result)
Output.to_excel(
    r"C:\\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\01.ChiNextTMT_300001-301235_20220225_EntityIdentification0000.xlsx",
    index=False, header=False)
