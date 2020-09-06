# -*- coding: utf-8 -*-

import seaborn as sns

titanic = sns.load_dataset('titanic')

mask1 = (titanic.age >= 10) & (titanic['age'] < 20) #둘다 같은 방법
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head(),'\n')

#나이가 10세미만이고 여성인 승객만 따로 선택
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head(), '\n')

#나이가 10세미만 또는 60세 이상인 승객의 age, sex, alone 열만 선택
mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morethan60 = titanic.loc[mask3,['age','sex','alone']]
print(df_under10_morethan60.head(), '\n')

