import numpy as np

theta = np.random.rand(5)

for _ in range(100):
    grad = np.random.rand(5)
    theta += 0.01 * grad

print(theta)
