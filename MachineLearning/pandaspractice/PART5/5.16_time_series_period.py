# -*- coding: utf-8 -*-

import pandas as pd

#날짜 형식의 문자열로 구성되는 리스트 정의
dates = ['2019-01-01','2020-03-01','2021-06-01']

#문자열의 배열(시리즈 객체)을 판다스 Timestamp로 변환
ts_dates = pd.to_datetime(dates)
print(ts_dates)
print('\n')

#Timestamp를 Period 로 변환
pr_day = ts_dates.to_period(freq='D')   #1일
print(pr_day)
pr_month = ts_dates.to_period(freq='M') #월말
print(pr_month)
pr_year = ts_date.to_period(freq='A')   #연말
print(pr_year)
