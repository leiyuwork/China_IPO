import pandas as pd  # データ解析を容易にする機能を提供する
import time

import requests
from bs4 import BeautifulSoup
import time
import os

from random import randint

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

for code in range(300001, 300080):
    random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
    headers = {
        'User-Agent': random_agent,
        # 'cookie': '__FTabcjffgh=2022-2-10-15-3-37; __NRUabcjffgh=1644473017108; __RECabcjffgh=1; __RTabcjffgh=2022-2-17-16-5-59'
    }
    url = "https://vip.stock.finance.sina.com.cn/corp/go.php/vCI_CorpManager/stockid/" + str(code) + ".phtml"
    print("********" + str(code) + "処理中*************")
    try:
        response = requests.get(url, headers=headers)
        time.sleep(5)
        soup = BeautifulSoup(response.text, 'html.parser')  # get the webpage content

        tables = soup.find('div', {"id": "con02-6"}).find_all('table')
        lijiegaoguan = tables[0].find_all('tr')
        gaoguan_number = 0
        for gaoguans in lijiegaoguan[2:]:
            gaoguan_number += 1
            result_gaoguan = [code, "G"]
            gaoguan_name = gaoguans.find_all('td')[0].text.strip()
            gaoguan_position = gaoguans.find_all('td')[1].text
            gaoguan_position_from = gaoguans.find_all('td')[2].text
            gaoguan_position_to = gaoguans.find_all('td')[3].text
            gaoguan_jianli_url = "https://vip.stock.finance.sina.com.cn" + \
                                 gaoguans.find_all('td')[0].find('a', href=True).attrs['href']
            gaoguan_jianli_url = gaoguan_jianli_url.encode('ascii', 'ignore').decode('ascii').replace(" ", "%20")
            try:
                gaoguan_dfs = pd.read_html(gaoguan_jianli_url)
                gaoguan_xingbie = gaoguan_dfs[13].iloc[0][1]
                gaoguan_birth = gaoguan_dfs[13].iloc[0][2]
                gaoguan_xueli = gaoguan_dfs[13].iloc[0][3]
                gaoguan_guoji = gaoguan_dfs[13].iloc[0][4]
                gaoguan_jianli = gaoguan_dfs[13].iloc[1][1]

                result_gaoguan.append(gaoguan_number)
                result_gaoguan.append(gaoguan_name)
                result_gaoguan.append(gaoguan_position)
                result_gaoguan.append(gaoguan_position_from)
                result_gaoguan.append(gaoguan_position_to)
                result_gaoguan.append(gaoguan_jianli_url)
                result_gaoguan.append(gaoguan_xingbie)
                result_gaoguan.append(gaoguan_birth)
                result_gaoguan.append(gaoguan_xueli)
                result_gaoguan.append(gaoguan_guoji)
                result_gaoguan.append(gaoguan_jianli)
            except Exception as e1:
                result_gaoguan.append(gaoguan_number)
                result_gaoguan.append(gaoguan_name)
                result_gaoguan.append(gaoguan_position)
                result_gaoguan.append(gaoguan_position_from)
                result_gaoguan.append(gaoguan_position_to)
                result_gaoguan.append(gaoguan_jianli_url)
                result_gaoguan.append(str(e1))
                pass

            Result_gaoguan = pd.DataFrame([result_gaoguan])
            Result_gaoguan.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\ChiNextTMT.csv", mode='a',
                                  index=False, header=None, encoding="utf-8_sig")

            time.sleep(3)

        lijiedongshi = tables[2].find_all('tr')
        dongshi_number = 0
        for dongshis in lijiedongshi[2:]:
            if "起始日期" not in dongshis.text:
                dongshi_number += 1
                result_dongshi = [code, "D"]
                dongshi_name = dongshis.find_all('td')[0].text.strip()
                dongshi_position = dongshis.find_all('td')[1].text
                dongshi_position_from = dongshis.find_all('td')[2].text
                dongshi_position_to = dongshis.find_all('td')[3].text
                dongshi_jianli_url = "https://vip.stock.finance.sina.com.cn" + \
                                     dongshis.find_all('td')[0].find('a', href=True).attrs['href']
                dongshi_jianli_url = dongshi_jianli_url.encode('ascii', 'ignore').decode('ascii').replace(" ", "%20")
                try:
                    dongshi_dfs = pd.read_html(dongshi_jianli_url)
                    dongshi_xingbie = dongshi_dfs[13].iloc[0][1]
                    dongshi_birth = dongshi_dfs[13].iloc[0][2]
                    dongshi_xueli = dongshi_dfs[13].iloc[0][3]
                    dongshi_guoji = dongshi_dfs[13].iloc[0][4]
                    dongshi_jianli = dongshi_dfs[13].iloc[1][1]

                    result_dongshi.append(dongshi_number)
                    result_dongshi.append(dongshi_name)
                    result_dongshi.append(dongshi_position)
                    result_dongshi.append(dongshi_position_from)
                    result_dongshi.append(dongshi_position_to)
                    result_dongshi.append(dongshi_jianli_url)
                    result_dongshi.append(dongshi_xingbie)
                    result_dongshi.append(dongshi_birth)
                    result_dongshi.append(dongshi_xueli)
                    result_dongshi.append(dongshi_guoji)
                    result_dongshi.append(dongshi_jianli)
                except Exception as e2:
                    result_dongshi.append(dongshi_number)
                    result_dongshi.append(dongshi_name)
                    result_dongshi.append(dongshi_position)
                    result_dongshi.append(dongshi_position_from)
                    result_dongshi.append(dongshi_position_to)
                    result_dongshi.append(dongshi_jianli_url)
                    result_dongshi.append(str(e2))
                    pass


                Result_dongshi = pd.DataFrame([result_dongshi])
                Result_dongshi.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\ChiNextTMT.csv", mode='a',
                                      index=False, header=None, encoding="utf-8_sig")
                time.sleep(3)

        lijiejianshi = tables[4].find_all('tr')
        jianshi_number = 0
        for jianshis in lijiejianshi[2:]:
            if "起始日期" not in jianshis.text:
                jianshi_number += 1
                result_jianshi = [code, "J"]
                jianshi_name = jianshis.find_all('td')[0].text.strip()
                jianshi_position = jianshis.find_all('td')[1].text
                jianshi_position_from = jianshis.find_all('td')[2].text
                jianshi_position_to = jianshis.find_all('td')[3].text
                jianshi_jianli_url = "https://vip.stock.finance.sina.com.cn" + \
                                     jianshis.find_all('td')[0].find('a', href=True).attrs['href']
                jianshi_jianli_url = jianshi_jianli_url.encode('ascii', 'ignore').decode('ascii').replace(" ", "%20")

                try:
                    jianshi_dfs = pd.read_html(jianshi_jianli_url)
                    jianshi_xingbie = jianshi_dfs[13].iloc[0][1]
                    jianshi_birth = jianshi_dfs[13].iloc[0][2]
                    jianshi_xueli = jianshi_dfs[13].iloc[0][3]
                    jianshi_guoji = jianshi_dfs[13].iloc[0][4]
                    jianshi_jianli = jianshi_dfs[13].iloc[1][1]

                    result_jianshi.append(jianshi_number)
                    result_jianshi.append(jianshi_name)
                    result_jianshi.append(jianshi_position)
                    result_jianshi.append(jianshi_position_from)
                    result_jianshi.append(jianshi_position_to)
                    result_jianshi.append(jianshi_jianli_url)
                    result_jianshi.append(jianshi_xingbie)
                    result_jianshi.append(jianshi_birth)
                    result_jianshi.append(jianshi_xueli)
                    result_jianshi.append(jianshi_guoji)
                    result_jianshi.append(jianshi_jianli)
                except Exception as e3:
                    result_jianshi.append(jianshi_number)
                    result_jianshi.append(jianshi_name)
                    result_jianshi.append(jianshi_position)
                    result_jianshi.append(jianshi_position_from)
                    result_jianshi.append(jianshi_position_to)
                    result_jianshi.append(jianshi_jianli_url)
                    result_jianshi.append(str(e3))

                Result_jianshi = pd.DataFrame([result_jianshi])
                Result_jianshi.to_csv(r"C:\Users\Ray94\OneDrive\Research\PHD\Research\data\PC\ChiNextTMT.csv", mode='a',
                                      index=False, header=None, encoding="utf-8_sig")
                time.sleep(3)
    except Exception as e:
        print(code, e)
        pass
