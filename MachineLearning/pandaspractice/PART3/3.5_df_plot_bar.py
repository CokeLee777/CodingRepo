# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('./남북한발전전력량.xlsx')

df_ns = df.iloc[[0,5], 3:]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)

#행 열 전치하여 막대그래프 그리기
tdf_ns = df_ns.T        #행 열 전치
print(tdf_ns.head())    #첫 5행만 보여준다.
print('\n')

tdf_ns.plot(kind='bar')