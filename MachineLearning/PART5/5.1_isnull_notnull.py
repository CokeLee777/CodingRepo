# -*- coding: utf-8 -*-

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')

#deck 열에 NaN 갯수 계산
nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
#누락 데이터 여부를 찾는법 (True or False)
print(df.head().isnull())
print(df.head().isnull().sum(axis=0))#누락 데이터 갯수 계산
print(df.head().notnull())