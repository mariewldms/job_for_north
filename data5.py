#datamining 통한 채용 합격 예측
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.neural_network import MLPClassifier

#데이터전처리
ob_names =["서비스직","사무원","노동자","기술자","장사"]
school=["무관", "대졸", "고졸"]

df=pd.read_csv("기업채용정보.csv")
test_df=pd.DataFrame({
    '무관': [1, 0, 1, 1],
    '대졸': [0, 1, 0, 0],
    '고졸': [0, 0, 0, 0],
    '서비스직': [0, 1, 1, 1],
    '사무원': [1, 1, 1, 0],
    '노동자': [1, 1, 0, 0],
    '기술자': [0, 0, 1, 1],
    '장사': [1, 0, 0, 0]
})


columns=['Column8','Column9','Column10','Column11','Column12','Column13','Column14','Column15','Column16','Column17']
for i in range (5):
    df[ob_names[i]]=df[columns].apply(lambda row: 1 if any(ob_names[i] in str(cell) for cell in row) else 0, axis=1)

for i in range(3):
    df[school[i]]=df.apply(lambda row: 1 if school[i] in row['Column3'] else 0, axis=1)


df=df[["무관","대졸","고졸","서비스직","사무원","노동자","기술자","장사","채용"]]

#데이터분석

#데이터 나누기
X_train=df.drop("채용",axis=1)
y_train=df["채용"]
X_test=test_df

forest_model = RandomForestClassifier(n_estimators = 100, random_state=100, 
                                max_depth = 30, min_samples_leaf = 4, 
                                min_samples_split = 4, oob_score=True)
gradient_model=GradientBoostingClassifier(n_estimators=150,learning_rate=0.1,max_depth=5,max_features='log2',random_state=100)
MLP_model = MLPClassifier(random_state=100, hidden_layer_sizes=(10),max_iter=2000)
ensemble_model = VotingClassifier(estimators=[('rf', forest_model), ('gb', gradient_model),('mlp',MLP_model)], voting='hard')
ensemble_model.fit(X_train, y_train)

#모델과 데이터 준비
X = df.drop("채용", axis=1)
y = df["채용"]

y_pred = ensemble_model.predict(X_test)
print(y_pred)