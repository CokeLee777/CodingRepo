# -*- coding: utf-8 -*-

import seaborn as sns

df = sns.load_dataset('titanic')

#반복문으로 각 열의 NaN 갯수 계산하기
missing_df = df.isnull()    #각 행,열의 값이 NaN이면 True, 없으면 False저장
for col in missing_df.columns:
    missing_count = missing_df[col].value_counts()  #True 는 1이므로 NaN의 갯수를 셀수있다
    
    try:
        print(col, ': ', missing_count[True])   #NaN값이 있으면 갯수 출력
    except:
        print(col, ': ', 0)     #NaN 값이 없으면 0개 출력
        

#NaN값이 500 개 이상인 열을 모두 삭제 deck 열
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

#age 열에 나이 데이터가 없는 모든 행 삭제
#how='any' 는 NaN값이 하나라도 존재하면 삭제한다는 뜻이다.
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

