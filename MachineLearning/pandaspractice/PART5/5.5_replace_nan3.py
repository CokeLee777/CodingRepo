# -*- coding: utf-8 -*-
#이웃하고있는 값으로 바꾸기

import seaborn as sns

df = sns.load_dataset('titanic')

#embark_town 열의 829 행의 NaN데이터 출력
print(df['embark_town'][825:830])
print('\n')

#embark_town 열의 NaN값을 바로 앞에있는 828행의 값으로 변경하기
df['embark_town'].fillna(method='ffill', inplace=True)
print(df['embark_town'][825:830])

