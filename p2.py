import random
import copy

grid_size = 5

# ORIGINAL GRID (used for learning)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],   # dirt
    [0, 0, 0, 1, 0],   # dirt
    [0, 0, -1, 0, 0],  # obstacle
    [0, 0, 0, 0, 0]
]

actions = ['up', 'down', 'left', 'right']
gamma = 0.9

# ---------------- MOVE FUNCTION ----------------
def move(state, action):
    x, y = state
    
    if action == 'up':
        x -= 1
    elif action == 'down':
        x += 1
    elif action == 'right':
        y += 1
    elif action == 'left':
        y -= 1
        
    if x < 0 or x >= grid_size or y < 0 or y >= grid_size:
        return state
    
    return (x, y)

# ---------------- VALUE FUNCTION ----------------
V = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

# ---------------- VALUE ITERATION ----------------
def value_iteration():
    global V
    
    for _ in range(50):
        new_V = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
        
        for i in range(grid_size):
            for j in range(grid_size):
                state = (i, j)
                values = []
                
                for action in actions:
                    next_state = move(state, action)
                    
                    # STATIC reward (IMPORTANT)
                    reward = grid[next_state[0]][next_state[1]]
                    
                    x, y = next_state
                    val = reward + gamma * V[x][y]
                    values.append(val)
                
                new_V[i][j] = max(values)
        
        V = new_V

# ---------------- BEST ACTION ----------------
def get_best_action(state):
    best_action = None
    best_value = -999
    
    for action in actions:
        next_state = move(state, action)
        reward = grid[next_state[0]][next_state[1]]
        
        x, y = next_state
        val = reward + gamma * V[x][y]
        
        if val > best_value:
            best_value = val
            best_action = action
    
    return best_action

# ---------------- SIMULATION ----------------
def simulate():
    sim_grid = copy.deepcopy(grid)   # separate grid for cleaning
    
    state = (0, 0)
    total_reward = 0
    visited = set()
    
    for step in range(100):   # safety limit
        
        action = get_best_action(state)
        new_state = move(state, action)
        
        x, y = new_state
        
        # dynamic reward (clean dirt)
        if sim_grid[x][y] == 1:
            reward = 1
            sim_grid[x][y] = 0
        else:
            reward = sim_grid[x][y]
        
        print(f"Step {step}: {state} -> {action} -> {new_state}, Reward: {reward}")
        
        total_reward += reward
        state = new_state
        
        # loop detection
        if state in visited:
            print("Loop detected!")
            break
        visited.add(state)
        
        # check if all dirt cleaned
        clean = True
        for row in sim_grid:
            if 1 in row:
                clean = False
                break
        
        if clean:
            print("All dirt cleaned!")
            break
    
    print("Total Reward:", total_reward)

# ---------------- RUN ----------------
value_iteration()
simulate()