import numpy as np
import matplotlib.pyplot as plt

X = np.array([0.0, 1.0, 2.0, 2.5, 3.5, 4.0, 4.5, 6.0, 6.5, 7.0, 7.5, 8.5, 9.0, 9.5, 10.0])
y = np.array([3.0, 3.5, 5.5, 5.8, 7.3, 7.5, 8.5, 9.5, 10.5, 11.3, 12.0, 13.0, 13.5, 17.0, 20.0])

W = 0   # 기울기
b = 0   # 절편

lrate = 0.01    # 학습률
epochs = 1000   # 반복 횟수

n = float(len(X))   # 입력 데이터의 개수

# 경사 하강법
for i in range(epochs):
    y_pred = W * X + b  # 예측값
    dW = (2/n) * sum(X * (y_pred-y))
    db = (2/n) * sum(y_pred - y)
    W = W - lrate * dW  # 기울기 수정
    b = b - lrate * db  # 절편 수정
    
# 기울기와 절편 출력
print (W, b)

# 예측값 생성
y_pred = W * X +b

# 입력 데이터를 그래프 상에 찍기
plt.scatter(X, y)

# 예측값은 선그래프로 그림
plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='red')
plt.show()

