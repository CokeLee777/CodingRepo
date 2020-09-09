# -*- coding: utf-8 -*-
#더미변수
import pandas as pd
import numpy as np

df = pd.read_csv('./auto-mpg.csv', header=None)

df.columns=['mpg','cylinders','displacement','horsepower','weight',
            'acceleration','model year','origin','name']

#horsepower 열의 누락 데이터 ('?') 를 삭제하고 실수형으로 변환
df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

#np.histogram 함수로 3개의 bin 으로 구분할 경계값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)
print(bin_dividers)

#3개의 bin에 이름 지정
bin_name = ['저출력', '보통출력', '고출력']

#pd.cut 함수로 각 데이터를 3개의 bin 에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],   #데이터 배열
                      bins=bin_dividers,    #경계값 리스트
                      labels=bin_name,      #경계값 이름
                      include_lowest=True)  #첫 경계값 포함

#hp_bin 열의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))