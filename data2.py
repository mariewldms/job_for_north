#탈북자 선택하기에 적절한 직업 순위(성별, 연령대 무관)
import pandas as pd
import numpy as np

jobInNorth=pd.read_csv("북한에서의_직업_20240917201907.csv")
jobIn3rd=pd.read_csv("제3국에서의_직업_20240917201922.csv")
learnSouth=pd.read_csv("직업교육훈련_경험_여부_및_분야_20240917202814.csv")
jobInSouth=pd.read_csv("직업유형_20240917203048.csv")

def findArray(csvFile,match,startWith,new,total):
    csvFile=csvFile.loc[csvFile["특성별(2)"]=='소계'].values[0]
    csvFile=csvFile[startWith:]
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

northMatch=[0,1,3,8,1,1,7,5,4,2,8,6]
thirdMatch=[0,3,2,6,1]
learnMatch=[4,1,0,5,5,5]
southMatch=[2,0,100,5,5,1,1,6,3,8]
job_names=["서비스직","사무원","노동자","농업어업","보건의료","공학기술자","장사","문화예술","군인"]

df=pd.DataFrame({
    "직업명":job_names,
    "a":findArray(jobInNorth,northMatch,3,north,58.1),
    "b":findArray(jobIn3rd,thirdMatch,5,third,33.3),
    "c":findArray(learnSouth,learnMatch,4,learn,122.8),
    "d":findArray(jobInSouth,southMatch,2,south,100.2)
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
print("\n순위에 따른 직업 정렬:")
print(df_sorted[['직업명', '총점', '순위']])

#서비스직, 장사, 사무원, 공학기술자, 노동자
#06152