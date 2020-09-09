# -*- coding: utf-8 -*-

import pandas as pd

#여러개의 데이터프레임을 하나의 엑셀파일에 저장

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A", "A+", "A"],
        'basic': ["A", "C", "A+"],
        'c++': ["A+", "A", "A+"],
        }

data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c2':[7,8,9],
         'c3':[10,11,12],
         'c4':[13,14,15],
         'c5':[16,17,18],
         }

df1 = pd.DataFrame(data)
df1.set_index('name', inplace=True)
df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)

#df1 을 'sheet1'으로 df2 를 'sheet2' 으로 저장
writer = pd.ExcelWriter("./df_excelwriter.xlsx")    #excel 워크북 객체를 생성(엑셀 파일)
df1.to_excel(writer, sheet_name='sheet1')   #sheet1 에 저장
df2.to_excel(writer, sheet_name='sheet2')   #sheet2 에 저장
writer.save()