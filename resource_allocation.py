import numpy as np

resources = 10

for _ in range(5):
    demand = np.random.randint(1,5)
    allocation = min(resources, demand)
    resources -= allocation
    print("Allocated:", allocation, "Remaining:", resources)
