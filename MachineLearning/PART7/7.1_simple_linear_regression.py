# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''
[step 1] 데이터 준비
'''

#csv 파일을 데이터프레임으로 변환
df = pd.read_csv('./auto-mpg.csv',header=None)

#열 이름 지정
df.columns=['mpg','cylinders','displacement','horsepower','weight',
            'acceleration','model year','origin','name']

#데이터 살펴보기
print(df.head(), '\n')

#IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기
pd.set_option('display.max_columns', 10)
print(df.head(), '\n')

'''
[step 2] 데이터 분석
'''

#데이터 자료형 확인
print(df.dtypes)

#horsepower 열의 자료형 변경(문자열 -> 숫자)
print(df.horsepower.unique(), '\n')

#'?' 데이터를 삭제
df.horsepower.replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df.horsepower = df.horsepower.astype('float')

print(df.describe(), '\n')

'''
[step 3] 속성 선택
'''

#분석에 활용할 열(속성) 선택
ndf = df[['mpg','cylinders','horsepower','weight']]
print(ndf.head())

#종속변수 Y인 연비(mpg) 와 다른변수 간의 선형관계를 그래프(산점도) 로 확인
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10,5))
plt.show()
plt.close()

#seaborn 으로 산점도 그리기
fig = plt.figure(figsize=(10,5))
