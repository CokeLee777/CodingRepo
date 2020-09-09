# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame([[15,'남','덕영중'], [17,'여','수리중']],
                  index=['준서', '예은'],   #행 이름 
                  columns=['나이','성별','학교']) # 열 이름

print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
print('\n')

df.index=['학생1', '학생2']
df.columns=['연령', '남녀', '소속']

print(df)

#rename(index={기존인덱스:새 인덱스, ...})
#rename(columns={기존인덱스:새 인덱스, ...})
#마지막에 inplace=True 를 붙여야 원본 객체가 변경된다.
df.rename(index={'학생1':'준서', '학생2':'예은'}, inplace=True)
df.rename(columns={'연령':'나이', '남녀':'성별', '소속':'학교'}, inplace=True)

print(df)

