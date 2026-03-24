# Autonomous Cleaning Robot (Fixed Version)

GRID_SIZE = 5
ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# 0 = empty, 1 = dirt, -1 = obstacle
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, -1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, -1, 0],
    [1, 0, 0, 0, 0]
]

gamma = 0.9
step_cost = -0.04


# -------------------------
# MOVE FUNCTION
# -------------------------
def move(pos, action):
    r, c = pos

    if action == 'UP':
        r = max(r - 1, 0)
    elif action == 'DOWN':
        r = min(r + 1, GRID_SIZE - 1)
    elif action == 'LEFT':
        c = max(c - 1, 0)
    elif action == 'RIGHT':
        c = min(c + 1, GRID_SIZE - 1)

    return (r, c)


# -------------------------
# VALUE ITERATION
# -------------------------
def value_iteration(grid, iterations=100):
    V = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    for _ in range(iterations):
        new_V = [row[:] for row in V]

        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):

                if grid[r][c] == -1:
                    continue

                values = []

                for action in ACTIONS:
                    nr, nc = move((r, c), action)

                    reward = step_cost

                    if grid[nr][nc] == -1:
                        reward = -1
                        nr, nc = r, c
                    elif grid[nr][nc] == 1:
                        reward = 1

                    val = reward + gamma * V[nr][nc]
                    values.append(val)

                new_V[r][c] = max(values)

        V = new_V

    return V


# -------------------------
# BEST ACTION
# -------------------------
def best_action(pos, V, grid):
    r, c = pos

    best_a = None
    best_val = -float('inf')

    for action in ACTIONS:
        nr, nc = move((r, c), action)

        reward = step_cost

        if grid[nr][nc] == -1:
            reward = -1
            nr, nc = r, c
        elif grid[nr][nc] == 1:
            reward = 1

        val = reward + gamma * V[nr][nc]

        if val > best_val:
            best_val = val
            best_a = action

    return best_a


# -------------------------
# PRINT VALUE FUNCTION
# -------------------------
def print_values(V):
    print("\nValue Function:\n")
    for row in V:
        for val in row:
            print(f"{val:.2f}", end="  ")
        print()


# -------------------------
# CHECK IF ALL CLEANED
# -------------------------
def all_cleaned(grid):
    for row in grid:
        if 1 in row:
            return False
    return True


# -------------------------
# SIMULATION
# -------------------------
def simulate():
    pos = (0, 0)
    total_reward = 0

    V = value_iteration(grid)
    print_values(V)

    print("\nRobot Movement:\n")

    step = 0
    while not all_cleaned(grid) and step < 50:

        action = best_action(pos, V, grid)
        new_pos = move(pos, action)

        r, c = new_pos
        reward = step_cost

        if grid[r][c] == -1:
            reward = -1
            new_pos = pos

        elif grid[r][c] == 1:
            reward = 1
            grid[r][c] = 0   # clean dirt

            # 🔥 recompute values after cleaning
            V = value_iteration(grid)
            print("\nUpdated Value Function after cleaning:\n")
            print_values(V)

        total_reward += reward
        pos = new_pos

        print(f"Step {step}: {action} → {pos} | Reward: {reward}")

        step += 1

    print("\nAll dirt cleaned!")
    print("Total Reward:", total_reward)


# -------------------------
# RUN
# -------------------------
if __name__ == "__main__":
    simulate()