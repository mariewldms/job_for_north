import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False


job_names =["서비스직","사무원","노동자","공학기술자","장사"]
age_groups = ["20대", "30대", "40대", "50대", "60대 이상"]


data = np.array([
 [21.4,  9.6, 11.5, 14.3, 13.5], #20대
 [22.1, 16.9,  9.9, 14.4, 11.4], #30대
 [24.9, 16.9, 14.8, 14.8,  6.7], #40대
 [26.6, 10.5, 16.3, 13.1,  6.7], #50대
 [26.8,  9.3, 17.9, 13.2,  4.7]  #60대
])


fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

angles = np.linspace(0, 2 * np.pi, 5, endpoint=False).tolist()
angles += angles[:1]

for i, age in enumerate(age_groups):
    normalized_data = data[i] / np.max(data[i])
    normalized_data = np.concatenate((normalized_data, [normalized_data[0]]))
    
    # 오각형 그리기
    ax.plot(angles, normalized_data, label=age)
    ax.fill(angles, normalized_data, alpha=0.25)


ax.set_xticks(angles[:-1])
ax.set_xticklabels(job_names)
ax.set_title('북한이탈주민 연령대에 따른 한국에서의 직무 추천')
plt.legend(loc='lower left', bbox_to_anchor=(1.0,0.5))

plt.show()
