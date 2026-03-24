import numpy as np

robots = [(0,0), (1,1)]

for _ in range(5):
    robots = [(r[0]+1, r[1]+1) for r in robots]
    print("Robot Positions:", robots)
