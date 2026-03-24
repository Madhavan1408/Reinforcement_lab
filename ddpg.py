import numpy as np

state_dim = 1
action_dim = 1

actor = np.random.rand(state_dim)
critic = np.random.rand(state_dim)

lr = 0.01

for _ in range(100):
    state = np.random.rand()
    action = actor * state

    reward = -(state - action)**2

    critic += lr * (reward - critic)
    actor += lr * critic * state

print("Actor:", actor)
