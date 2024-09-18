import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

#data clustering
twenty=[21.4,  9.6, 11.5, 14.3, 13.5]
thirty=[22.1, 16.9,  9.9, 14.4, 11.4]
fourty=[24.9, 16.9, 14.8, 14.8,  6.7]
fifty=[26.6, 10.5, 16.3, 13.1,  6.7]
sixty=[26.8,  9.3, 17.9, 13.2,  4.7]
job=["서비스직","사무원","노동자","공학기술자","장사"]

# 데이터프레임 생성
df = pd.DataFrame({
    '직업명': job,
    '20대': twenty,
    '30대': thirty,
    '40대': fourty,
    '50대': fifty,
    '60대 이상': sixty
})

# 직업별 연령대 선호도 데이터로 클러스터링
data = df[['20대', '30대', '40대', '50대','60대 이상']].values

# KMeans 클러스터링
kmeans = KMeans(n_clusters=3, random_state=0).fit(data)

# 클러스터 결과를 데이터프레임에 추가
df['클러스터'] = kmeans.labels_

# 클러스터링 결과 출력
print(df[['직업명', '클러스터']])

# 클러스터 시각화
from sklearn.decomposition import PCA
pca = PCA(2)  # 2차원으로 축소
data_2d = pca.fit_transform(data)

plt.scatter(data_2d[:, 0], data_2d[:, 1], c=kmeans.labels_, cmap='viridis')
for i, job in enumerate(job):
    plt.text(data_2d[i, 0], data_2d[i, 1], job)
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.title('연령대에 따른 탈북이탈주민 직업 추천')
plt.show()