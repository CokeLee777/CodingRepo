# -*- coding: utf-8 -*-
#정규화
import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg','cylinders','displacement','horsepower','weight',
            'acceleration','model year','origin','name']

df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'],axis=0,inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

#horsepower 열의 통계요약정보로 최대값 확인
print(df.horsepower.describe())
print('\n')

#horsepower 열의 최대값의 절대값으로 모든 데이터를 나눠서 저장
df.horsepower = df.horsepower/abs(df.horsepower.max())

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())

#horsepower 열의 최대값과 절대값으로 모든 데이터를 나눠서 저장
min_x = df.horsepower - df.horsepower.min()
min_max = df.horsepower.max() - df.horsepower.min()
df.horsepower = min_x/min_max

print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())

