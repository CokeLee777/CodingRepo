# -*- coding: utf-8 -*-

import pandas as pd

#read_csv() 메소드로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

#열 이름 지정
df.columns=['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
            'acceleration', 'model year', 'origin', 'name']

print(df.head())    #처음 5개 행을 보여준다.
print('\n')
print(df.tail())    #마지막 5개 행을 보여준다.
print('\n')

print(df.shape) #행 열의 갯수를 호출
print('\n')
print(df.info())    #데이터프레임 df 에 관한 기본정보 출력
print('\n')

print(df.dtypes)    #각 열의 자료형 확인
print('\n')
print(df.mpg.dtypes)    #mpg열의 자료형 확인
print('\n')

#데이터프레임 df 의 기술통계정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))#열에대한 정보까지 포함(unique:고유값 개수, top:최빈값, freq:빈도수)