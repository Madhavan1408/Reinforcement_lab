import numpy as np

theta = np.random.rand()

def policy(theta):
    return 1 / (1 + np.exp(-theta))

for _ in range(100):
    prob = policy(theta)
    reward = np.random.rand()
    gradient = reward * (1 - prob)
    theta += 0.01 * gradient

print("Optimized Theta:", theta)
