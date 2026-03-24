import numpy as np

def reward(action):
    if action == "harm":
        return -10
    return 1

actions = ["safe", "harm"]

for _ in range(10):
    action = np.random.choice(actions)
    r = reward(action)
    print(action, r)
