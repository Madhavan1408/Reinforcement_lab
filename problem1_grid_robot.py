import numpy as np
import random

grid_size = 5
grid = np.zeros((grid_size, grid_size))

grid[1][2] = 1
grid[3][3] = 1
grid[2][1] = -1
grid[4][0] = -1

actions = [(0,1),(1,0),(0,-1),(-1,0)]

def is_valid(x, y):
    return 0 <= x < grid_size and 0 <= y < grid_size

def simulate():
    x, y = 0, 0
    total_reward = 0
    for _ in range(20):
        action = random.choice(actions)
        nx, ny = x + action[0], y + action[1]
        if is_valid(nx, ny):
            x, y = nx, ny
            total_reward += grid[x][y]
    print("Total Reward:", total_reward)

simulate()
