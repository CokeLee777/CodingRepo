# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

#열 이름 지정
df.columns=['mpg','cylinders','displacement','horsepower','weight',
            'acceleration','model year','origin','name']

#각 열의 자료형 확인
print(df.dtypes)
print('\n')

#horsepower 열의 고유값 확인
print(df['horsepower'].unique())    #문자열
print('\n')

#누락데이터('?') 삭제 -> NaN값으로 변경함
df['horsepower'].replace('?', np.nan, inplace=True)     #horsepower열의 ? 값을 NaN값으로 바꾼다
df.dropna(subset=['horsepower'], axis=0, inplace=True)  #horsepower열의 NaN값을 버린다
df['horsepower'] = df['horsepower'].astype('float') #문자열을 실수형으로 변경

print(df['horsepower'].unique())    #실수형
print(df['horsepower'].dtypes)
print('\n')

#origin 열의 고유값 확인
print(df['origin'].unique())

#origin 열의 자료형을 문자형으로 변경    astype 대신에 각각을 모두 바꿔주어도 자료형이 변경된다.
df['origin'].replace({1:'USA',2:'EU',3:'JPN'}, inplace=True)

print(df['origin'].unique())
print(df['origin'].dtypes)
print('\n')

#문자형을 범주형으로 변경
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

#범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)
print('\n')

#model year 열의 정수형을 범주형으로 변환
df['model year'] = df['model year'].astype('category')
print(df['model year'].unique())
print('\n')
print(df['model year'].dtypes)