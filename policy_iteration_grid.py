import numpy as np

V = np.zeros((4,4))
gamma = 0.9

for _ in range(50):
    for i in range(4):
        for j in range(4):
            V[i][j] = max([gamma*V[i][j] - 1])

print(V)
