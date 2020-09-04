# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv('./auto-mpg.csv', header=None)

#열 이름 저장
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              'acceleration', 'model year', 'origin', 'name']

#열을 선택하여 박스 플롯 그리기
df[['mpg', 'cylinders']].plot(kind='box')
