# -*- coding: utf-8 -*-

#라이브러리 불러오기
import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

#위키피디아 미국 ETF 웹 페이지에서 필요한 정보를 스크래핑하여 딕셔너리 형태로 변수 etfs 에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
rows = soup.select('dix > ul > li')

#빈 딕셔너리 자료형 만들기
etfs = {}

for row in rows:
    
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        
        if(len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_ticker) > 0):
            #빈 딕셔너리에 key 값이 'etf_ticker[0]' 이고 데이터값이  [etf_market[0], etf_name[0]] 인 데이터 삽입
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
            
    except AttributeError as err:
        pass
    

#etfs 딕셔너리 출력
print(etfs)
print('\n')

df = pd.DataFrame(etfs)
print(df)


