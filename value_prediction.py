import numpy as np
from sklearn.linear_model import LinearRegression

X = np.random.rand(100, 3)
y = np.sum(X, axis=1) + np.random.randn(100)*0.1

model = LinearRegression()
model.fit(X, y)

print(model.predict(X[:5]))
