import numpy as np

global_value = 0

def worker():
    global global_value
    for _ in range(10):
        reward = np.random.rand()
        global_value += 0.01 * reward

for _ in range(5):
    worker()

print("Global Value:", global_value)
