gamma = 0.9
states = range(5)
V = [0]*5

for _ in range(50):
    for s in states:
        if s == 4:
            V[s] = 1
        else:
            V[s] = gamma * V[s+1]

print(V)
