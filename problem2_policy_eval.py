import numpy as np

gamma = 0.9
states = [(i, j) for i in range(3) for j in range(3)]
V = {s: 0 for s in states}

def reward(state):
    if state == (2,2): return 5
    return -1

def next_states(s):
    moves = [(0,1),(1,0),(0,-1),(-1,0)]
    result = []
    for m in moves:
        ns = (s[0]+m[0], s[1]+m[1])
        if 0 <= ns[0] < 3 and 0 <= ns[1] < 3:
            result.append(ns)
    return result

for _ in range(50):
    new_V = V.copy()
    for s in states:
        new_V[s] = sum([reward(ns) + gamma*V[ns] for ns in next_states(s)]) / len(next_states(s))
    V = new_V

print(V)
