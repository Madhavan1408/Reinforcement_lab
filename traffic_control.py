import numpy as np

traffic = np.random.rand(10)

for _ in range(50):
    signal_time = np.mean(traffic)
    traffic = traffic + np.random.randn(10)*0.1
    traffic = np.clip(traffic, 0, 1)

print("Optimized Signal Time:", signal_time)
