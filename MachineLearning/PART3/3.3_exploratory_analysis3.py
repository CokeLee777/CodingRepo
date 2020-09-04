# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

#열 이름 지정
df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'acceleration', 'model year', 'origin', 'name']

#평균값 mean() 메서드 활용하여 각 열에대한 항목들의 평균값을 구함
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())
print('\n')

#중간값 median() 메서드 활용
print(df.median())
print('\n')
print(df.mpg.median())
print('\n')

#최대값 max() 메서드 활용
print(df.max())
print('\n')
print(df.origin.max())
print('\n')

#최소값 min() 메서드 활용
print(df.min())
print('\n')
print(df.weight.min())
print('\n')

#표준편차 std() 메서드 활용
print(df.std())
print('\n')
print(df.mpg.std())
print('\n')

#상관계수 corr() 메서드 활용
print(df.corr())
print('\n')
print(df[['mpg', 'weight']].corr())