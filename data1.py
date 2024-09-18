#프로젝트 동기: 현황 자료
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

yearList=[0]*5
addList=[0]*5

survey_df=pd.read_csv("탈북동기_20240917172324.csv")
year=2019
for i in range(5):
    year=str(year)
    yearList[i]=year
    col_year=[year+"_1",year+"_2",year+"_3"]
    print(col_year)
    value=survey_df.loc[survey_df['특성별(2)']=='소계',col_year].values[0]
    add=0
    for j in range(3):
        add+=float(value[j])
    print(add)
    addList[i]=add
    year=int(year)
    year+=1
print(addList)
plt.bar(yearList,addList, width=0.4, color='skyblue')
plt.title("")
plt.xlabel("year")
plt.ylabel("percentage")
plt.show()