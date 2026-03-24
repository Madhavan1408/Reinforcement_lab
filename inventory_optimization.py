import numpy as np

inventory = 50
cost = 0

for _ in range(30):
    demand = np.random.randint(10,30)
    if inventory < demand:
        order = 20
    else:
        order = 0
    inventory += order - demand
    cost += abs(inventory)

print("Total Cost:", cost)
