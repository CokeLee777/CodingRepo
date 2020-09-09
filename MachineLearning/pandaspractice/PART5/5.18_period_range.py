# -*- coding: utf-8 -*-

import pandas as pd

#Period 배열 만들기 1개월 길이
pr_m = pd.period_range('2019-01-01',
                       end=None,    #날짜범위의 끝을 따로 정하지않음
                       periods=3,   #3개 생성
                       freq='M')    #1개월마다반복생성

print(pr_m)

#Period 배열 만들기 1시간 길이
pr_h = pd.period_range('2019-01-01',
                       end=None,
                       periods=3,
                       freq='H')

print(pr_h)

#Period 배열 만들기 2시간 길이
pr_2h = pd.period_range('2019-01-01',
                        end=None,
                        periods=3,
                        freq='2H')

print(pr_2h)

