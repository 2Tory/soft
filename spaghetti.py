import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 랜덤 시드 설정하고 데이터 생성
np.random.seed(0)
data = np.random.randn(100, 2)


# 서브플롯 생성
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 서브플롯 1: 기술 통계
a, b = data[:, 0], data[:, 1]
axes[0, 0].bar(['Mean', 'Median'], [np.mean(a), np.median(a)], color='blue', alpha=0.7, label='Variable 1')
axes[0, 0].bar(['Mean', 'Median'], [np.mean(b), np.median(b)], color='green', alpha=0.7, label='Variable 2')
axes[0, 0].legend()
axes[0, 0].set_title('Descriptive Statistics: Mean and Median')

# 서브플롯 2: 상관 분석
sns.heatmap(np.corrcoef(data.T), annot=True, ax=axes[0, 1])
axes[0, 1].set_title('Correlation Analysis')

# 서브플롯 3: 변수의 히스토그램
axes[1, 0].hist(a, bins=15, color='blue', alpha=0.7, label='Variable 1')
axes[1, 0].hist(b, bins=15, color='green', alpha=0.7, label='Variable 2')
axes[1, 0].legend()
axes[1, 0].set_title('Histogram of Variables')

# 서브플롯 4: 산점도
axes[1, 1].scatter(a, b, alpha=0.7)
axes[1, 1].set_xlabel('Variable 1')
axes[1, 1].set_ylabel('Variable 2')
axes[1, 1].set_title('Scatter Plot of Variable 1 vs Variable 2')

# 레이아웃 조절 및 플롯 표시
plt.tight_layout()
plt.show()