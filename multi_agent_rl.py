import numpy as np

agents = [0, 0]

for _ in range(10):
    actions = [np.random.randint(0,2) for _ in agents]
    reward = 1 if sum(actions) == 2 else -1
    print("Actions:", actions, "Reward:", reward)
