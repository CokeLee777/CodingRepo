# -*- coding: utf-8 -*-

import pandas as pd

#해당 파일을 찾고 변수에 저장한다.
file_path = './read_csv_sample.csv'


#read_csv 함수로 데이터프레임 변환
df1 = pd.read_csv(file_path)
print(df1)
print('\n')


#read_csv 함수로 데이터프레임 변환
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

#행 인덱스를 지정하지 않음
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

#행 인덱스로 c0 을 사용 
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)
