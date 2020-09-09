# -*- coding: utf-8 -*-

import pandas as pd

#HTML 파일 경로 or 웹 페이지 주소를 url 변수에 저장
url = './sample.html'

#read_html() 함수로 데이터 프레임 변환
tables = pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print("tables[%s]" %i)
    print(tables[i])
    print('\n')
    
#두번째 데이터프레임에서 'name' 열을 인덱스로 지정
df = tables[1]
df.set_index('name', inplace=True)
print(df)