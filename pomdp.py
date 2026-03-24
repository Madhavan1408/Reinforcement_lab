import numpy as np

true_state = np.random.randint(0,5)

def observe(state):
    return state + np.random.randint(-1,2)

belief = 2

for _ in range(10):
    obs = observe(true_state)
    belief = (belief + obs) // 2
    print("Observation:", obs, "Belief:", belief)
