# -*- coding: utf-8 -*-

import pandas as pd

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "A"],
        'basic': ["A", "C", "A+"],
        'c++': ["A+", "A", "A+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)

df.to_excel('./df_sample.xlsx')
