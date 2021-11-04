import matplotlib.pylab as plt
from sklearn import linear_model
reg = linear_model.LinearRegression()

X = [[174], [152], [138], [128], [186], [164], [170], [145], [156], [180]]
y = [71, 55, 46, 38, 88, 62, 66, 42, 54, 78]
reg.fit(X, y)   # 학습

print(reg.predict([[165]]))

# 학습 데이터와 y 값을 산포도로 그림
plt.scatter(X, y, color='black')

# 학습 데이터를 입력으로 하여 예측값을 계산
y_pred = reg.predict(X)

# 학습 데이터와 예측값을 선그래프로 그림
# 계산된 기울기와 y절편을 가지는 직선이 그려짐
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()
