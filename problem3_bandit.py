import numpy as np

k = 5
true_rewards = np.random.rand(k)

def epsilon_greedy(epsilon=0.1, steps=1000):
    Q = np.zeros(k)
    N = np.zeros(k)

    for t in range(steps):
        if np.random.rand() < epsilon:
            a = np.random.randint(k)
        else:
            a = np.argmax(Q)

        reward = np.random.randn() + true_rewards[a]
        N[a] += 1
        Q[a] += (reward - Q[a]) / N[a]

    return sum(Q)

print("Epsilon-Greedy:", epsilon_greedy())
