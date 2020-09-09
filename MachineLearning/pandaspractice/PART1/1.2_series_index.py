# -*- coding: utf-8 -*-

import pandas as pd

#리스트를 시리즈로 변환하여 변수 sr 에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]

sr = pd.Series(list_data)
print(type(sr))
print('\n')
print(sr)

#실행 결과 인덱스는 0부터 순서대로 자리매겨지고 데이터값은 객체로 표시된다.

idx = sr.index
val = sr.values
print(idx)
print('\n')
print(val)