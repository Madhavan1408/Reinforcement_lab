import numpy as np
import random

Q = np.zeros((5,5,4))
alpha, gamma, epsilon = 0.1, 0.9, 0.1

def choose_action(s):
    if random.random() < epsilon:
        return random.randint(0,3)
    return np.argmax(Q[s[0], s[1]])

for _ in range(100):
    s = (0,0)
    a = choose_action(s)
    for _ in range(20):
        ns = (min(4,s[0]+1), min(4,s[1]+1))
        r = -1
        na = choose_action(ns)
        Q[s[0],s[1],a] += alpha*(r + gamma*Q[ns[0],ns[1],na] - Q[s[0],s[1],a])
        s, a = ns, na

print(Q)
