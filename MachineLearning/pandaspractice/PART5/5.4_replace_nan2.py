# -*- coding: utf-8 -*-

import seaborn as sns

df = sns.load_dataset('titanic')

#embark_town 열의 829행의 NaN데이터 출력
print(df['embark_town'][825:830])
print('\n')

#embark_town 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환
most_freq = df['embark_town'].value_counts(dropna=True).idxmax()
print(most_freq)
print('\n')

df['embark_town'].fillna(most_freq, inplace=True)
print(df['embark_town'][825:830])