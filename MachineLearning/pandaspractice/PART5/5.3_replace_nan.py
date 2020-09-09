# -*- coding: utf-8 -*-
#평균으로 누락 데이터 바꾸기
import seaborn as sns

df = sns.load_dataset('titanic')

#age 열의 첫 10개 데이터 출력(5행에 NaN값)
print(df['age'].head(10))
print('\n')

#age 열의 NaN 값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0)
df['age'].fillna(mean_age, inplace=True)
print(df['age'].head(10))
