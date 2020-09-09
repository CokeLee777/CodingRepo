# -*- coding: utf-8 -*-
#단위환산
import pandas as pd

#read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv',header=None)

#열 이름 지정
df.columns=['mpg','cylinders','displacement','horsepower','weight',
            'acceleration','model year','origin','name']

print(df.head())
print('\n')

#mpg 를 kpl 로 변환
mpg_to_kpl = 1.60934/3.78541

#mpg 열에 0.425를 곱한 결과를 새로운 열(kpl) 에 추가
df['kpl'] = df['mpg'] * mpg_to_kpl

#kpl 열을 소수점 아래 둘째자리에서 반올림
df['kpl'] = df['kpl'].round(2)
print(df.head())
