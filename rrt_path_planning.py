import numpy as np
import random

start = (0,0)
goal = (9,9)
tree = [start]

def distance(a,b):
    return np.linalg.norm(np.array(a)-np.array(b))

for _ in range(100):
    rand = (random.randint(0,10), random.randint(0,10))
    nearest = min(tree, key=lambda x: distance(x, rand))
    new = ((nearest[0]+rand[0])//2, (nearest[1]+rand[1])//2)
    tree.append(new)
    if distance(new, goal) < 2:
        print("Goal reached!")
        break

print(tree[:10])
