import numpy as np

policy = np.random.rand()

def reward(policy):
    return - (policy - 0.5)**2

for _ in range(100):
    grad = (reward(policy+0.01) - reward(policy)) / 0.01
    policy += 0.1 * grad

print("Optimal Policy:", policy)
