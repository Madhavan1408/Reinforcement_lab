import numpy as np

theta = np.random.rand(5,2)

def policy(state):
    p = np.exp(theta[state])
    return p / np.sum(p)

for _ in range(100):
    for s in range(5):
        probs = policy(s)
        action = np.argmax(probs)

        reward = 1 if s == 4 else -0.1

        advantage = reward
        theta[s][action] += 0.01 * advantage

print(theta)
