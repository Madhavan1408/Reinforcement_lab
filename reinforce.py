import numpy as np

states = 5
actions = 2
theta = np.random.rand(states, actions)

def softmax(x):
    e = np.exp(x - np.max(x))
    return e / np.sum(e)

def get_action(state):
    probs = softmax(theta[state])
    return np.random.choice(actions, p=probs)

alpha = 0.01
gamma = 0.9

for episode in range(100):
    trajectory = []
    state = 0

    for t in range(10):
        action = get_action(state)
        reward = 1 if state == states-1 else -0.1
        trajectory.append((state, action, reward))
        state = min(state+1, states-1)

    G = 0
    for t in reversed(range(len(trajectory))):
        s, a, r = trajectory[t]
        G = r + gamma * G
        probs = softmax(theta[s])
        theta[s][a] += alpha * G * (1 - probs[a])

print("Policy Learned:", theta)
