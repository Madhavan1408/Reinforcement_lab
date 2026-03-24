import numpy as np

def high_level(state):
    return "move_to_goal" if state < 5 else "finish"

def low_level(state):
    return state + 1

state = 0

for _ in range(10):
    task = high_level(state)
    if task == "move_to_goal":
        state = low_level(state)
    print("State:", state, "Task:", task)
