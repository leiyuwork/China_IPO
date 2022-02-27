import pandas as pd  # データ解析を容易にする機能を提供する
import time
import stanza

stanza.download('zh')
zh_nlp = stanza.Pipeline('zh', use_gpu=False, processors='tokenize,ner')

df = pd.read_excel(
    r'C:\\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\00.ChiNextTMT_300001-301235_20220225 - 処理用.xlsx')
all_list = df.values.tolist()

start = time.time()
i = 0
Result = []
for each_case in all_list:
    print(each_case[0], each_case[1], each_case[2])
    i = i + 1
    print("********ケース" + str(i) + "処理中*************")
    entity_result = [each_case[0], each_case[1], each_case[2], each_case[12]]
    text = each_case[12]
    doc = zh_nlp(text)
    for sent in doc.sentences:
        for entity in sent.ents:
            if entity.type == 'ORG':
                entity_result.append(entity.text)
    Result.append(entity_result)
Output = pd.DataFrame(Result)
Output.to_excel(
    r"C:\\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\01.ChiNextTMT_300001-301235_20220225_EntityIdentification.xlsx",
    index=False, header=False)
end = time.time()
print('程序执行时间: ', end - start)

