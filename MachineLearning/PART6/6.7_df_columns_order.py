# -*- coding: utf-8 -*-
#열 순서 바꾸기
import seaborn as sns

#titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4, 'survived':'age']
print(df)

#열 이름의 리스트 만들기
columns = list(df.columns.values)   #열이름의 값들을 가지고 리스트 생성
print(columns, '\n')

#열 이름을 알파벳 순서대로 정렬하기
columns_sorted = sorted(columns)    #알파벳 순서대로 정렬된 리스트
df_sorted = df[columns_sorted]      #정렬된 리스트를 데이터프레임으로 변환
print(df_sorted)

#열 이름을 기존 순서의 정반대 역순으로 정렬하기
columns_reversed = reversed(columns)
df_reversed = df[columns_reversed]
print(df_reversed)

#열 이름을 사용자가 정의한 임의의 순서로 재배치하기
columns_customed = ['pclass','sex','age','survived']
df_customed = df[columns_customed]
print(df_customed)

