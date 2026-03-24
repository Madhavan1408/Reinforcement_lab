import numpy as np

param = np.random.rand()

def task(x):
    return (x - 2)**2

for _ in range(100):
    grad = (task(param+0.01) - task(param)) / 0.01
    param -= 0.1 * grad

print("Learned Parameter:", param)
