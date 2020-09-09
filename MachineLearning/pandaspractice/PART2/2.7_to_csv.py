# -*- coding: utf-8 -*-

import pandas as pd

#판다스 DataFrame 함수로 데이터프레임 변환
data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B", "B+"],
        'c++': ["B+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)  #'name' 열을 인덱스로 지정
print(df)

#to_csv() 메소드를 이용하여 CSV 파일로 내보내기. 파일명을 df_sample.csv 로 저장
df.to_csv('./df_sample.csv')