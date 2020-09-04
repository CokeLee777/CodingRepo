# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'acceleration', 'model year', 'origin', 'name']

#데이터프레임 df의 각 열이 가지고있는 원소 갯수 확인
print(df.count())
print('\n')
print(type(df.count())) #시리즈 객체로 출력

#origin 열의 고유값 확인
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')

print(type(unique_values))
