import numpy as np

def primitive_action(state):
    return state + 1

def subtask(state):
    for _ in range(3):
        state = primitive_action(state)
    return state

state = 0
state = subtask(state)

print("Final State:", state)
