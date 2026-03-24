import numpy as np

states = 5
actions = 2

actor = np.random.rand(states, actions)
critic = np.zeros(states)

alpha = 0.01
gamma = 0.9

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

for episode in range(100):
    state = 0

    for step in range(10):
        probs = softmax(actor[state])
        action = np.random.choice(actions, p=probs)

        next_state = min(state+1, states-1)
        reward = 1 if next_state == states-1 else -0.1

        td_error = reward + gamma * critic[next_state] - critic[state]

        critic[state] += alpha * td_error
        actor[state][action] += alpha * td_error

        state = next_state

print("Actor:", actor)
print("Critic:", critic)
