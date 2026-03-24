import numpy as np

def environment(state, action):
    next_state = state + action + np.random.randn()*0.1
    reward = -abs(next_state)
    return next_state, reward

def model(state, action):
    return state + action

policy = 0.1
state = np.random.rand()

for _ in range(100):
    action = policy
    predicted_next = model(state, action)
    real_next, reward = environment(state, action)
    policy += 0.01 * reward
    state = real_next

print("Optimized Policy:", policy)
