# -*- coding: utf-8 -*-

import pandas as pd

#판다스 DataFrame 함수로 데이터프레임 변환
data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["C", "C+", "A"],
        'basic': ["C", "C", "C+"],
        'c++': ["C+", "C", "C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)

df.to_json('./df_sample.json')