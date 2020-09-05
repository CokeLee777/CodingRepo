# -*- coding: utf-8 -*-

import pandas as pd

df = pd.DataFrame({'c1':['a','a','b','a','b'],
                   'c2':[1,1,1,2,2],
                   'c3':[1,1,2,2,2]})
print(df)
print('\n')

#행이 아예 똑같아야 중복이라고 표시됨 (True)
df_dup = df.duplicated()
print(df_dup)
print('\n')

#특정열에서의 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)
print('\n')
