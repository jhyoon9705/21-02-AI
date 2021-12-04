# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 10:57:32 2021

@author: jhyoon
"""

x = 10
learning_rate = 0.1
precision = 0.00001
max_iterations = 100

# 손실 함수를 람다식으로 정의
loss_func = lambda x: (x-3)**2 + 10

# 그래디언트를 람다식으로 정의, 손실 함수의 1차 미분값임
gradient = lambda x: 2*x - 6

# 그래디언트 강하법
for i in range(max_iterations):
    x = x - learning_rate * gradient(x)
    print("손실 함수값(", x, ")=", loss_func(x))
    
print("최소값 = ", x)

