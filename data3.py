#서비스직, 장사, 사무원, 공학기술자, 노동자
#06152->01256
#배열 순서 재조정
#array=[서비스직,사무원,노동자,공학기술자,장사]

#data clustering 전처리
import pandas as pd
import numpy as np

jobInNorth=pd.read_csv("북한에서의_직업_20240917201907.csv")
jobIn3rd=pd.read_csv("제3국에서의_직업_20240917201922.csv")
learnSouth=pd.read_csv("직업교육훈련_경험_여부_및_분야_20240917202814.csv")
jobInSouth=pd.read_csv("직업유형_20240917203048.csv")

#06152남기고 제외 
age="60대 이상"

def findArray(csvFile,match,startWith,new):
    csvFile=csvFile.loc[csvFile["특성별(2)"]==age].values[0]
    csvFile=csvFile[startWith:]
    total=0
    for i in range(len(csvFile)):
        total+=csvFile[i]
    for i in range(len(match)):
        csvFile[i]=int(csvFile[i]/total*100)
        if (match[i]==100):
            continue
        new[match[i]]+=csvFile[i]
    return new

north=[0]*9
third=[0]*9
learn=[0]*9
south=[0]*9

northMatch=[0,1,100,100,1,1,100,5,100,2,100,6]
thirdMatch=[0,100,2,6,1]
learnMatch=[100,1,0,5,5,5]
southMatch=[2,0,100,5,5,1,1,6,100,100]
job_names=["서비스직","사무원","노동자",0,0,"공학기술자","장사",0,0]


df=pd.DataFrame({
    "직업명":job_names,
    "a":findArray(jobInNorth,northMatch,3,north),
    "b":findArray(jobIn3rd,thirdMatch,5,third),
    "c":findArray(learnSouth,learnMatch,4,learn),
    "d":findArray(jobInSouth,southMatch,2,south)
})


#데이터처리
weights=[0.2,0.1,0.2,0.5]
df['총점'] = (
    df['a'] * weights[0] +
    df['b'] * weights[1] +
    df['c'] * weights[2] +
    df['d'] * weights[3]
)


df['순위']=df['총점'].rank(ascending=False)
df_sorted = df.sort_values(by='순위')
print("\n순위에 따른 직업 정렬:"+age)
print(df_sorted[['직업명', '총점', '순위']])
print(np.delete(df["총점"].to_numpy(),[3,4,7,8]))