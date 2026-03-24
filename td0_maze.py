import numpy as np

gamma = 0.9
V = np.zeros(5)

for _ in range(100):
    for s in range(4):
        V[s] += 0.1 * (-1 + gamma * V[s+1] - V[s])

print(V)
