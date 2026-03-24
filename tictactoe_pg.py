import numpy as np

Q = np.zeros((9,9))

for _ in range(1000):
    state = 0
    for step in range(5):
        action = np.random.randint(9)
        reward = 1 if action == 8 else 0
        Q[state][action] += 0.1 * (reward - Q[state][action])

print(Q)
