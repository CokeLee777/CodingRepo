# -*- coding: utf-8 -*-

import pandas as pd

#Timestamp 배열 만들기 -월 간격, 월의 시작일 기준
ts_ms = pd.date_range(start='2019-01-01',   #날짜범위시작
                      end=None,             #날짜범위 끝
                      periods=6,            #생성할 Timestamp 개수
                      freq='MS',            #시간간격(MS: 월초)
                      tz='Asia/Seoul')      #시간대(timezone)

print(ts_ms)

#분기 (3개월) 간격, 월의 마지막 날 기준
ts_3m = pd.date_range('2019-01-01',
                      periods=6,
                      freq='3M',    #3월마다 월말
                      tz='Asia/Seoul')

print(ts_3m)