import numpy as np
import random

Q = np.zeros((5,5,4))
alpha, gamma, epsilon = 0.1, 0.9, 0.1

for _ in range(100):
    s = (0,0)
    for _ in range(20):
        if random.random() < epsilon:
            a = random.randint(0,3)
        else:
            a = np.argmax(Q[s[0],s[1]])

        ns = (min(4,s[0]+1), min(4,s[1]+1))
        r = -1

        Q[s[0],s[1],a] += alpha*(r + gamma*np.max(Q[ns[0],ns[1]]) - Q[s[0],s[1],a])
        s = ns

print(Q)
