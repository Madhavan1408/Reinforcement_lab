import numpy as np

gamma = 0.9
grid_size = 4
V = np.zeros((grid_size, grid_size))

actions = [(0,1),(1,0),(0,-1),(-1,0)]

def reward(s):
    return -1

for _ in range(50):
    for i in range(grid_size):
        for j in range(grid_size):
            values = []
            for a in actions:
                ni, nj = i+a[0], j+a[1]
                if 0 <= ni < grid_size and 0 <= nj < grid_size:
                    values.append(reward((ni,nj)) + gamma * V[ni][nj])
            V[i][j] = max(values)

print(V)
