import numpy as np
import random

class GridMDP:
    def __init__(self, size=5, dirt_cells=None, obstacle_cells=None, start=(0,0)):
        self.size = size
        self.start = start
        self.state = start
        
        # Define dirt and obstacles
        self.dirt_cells = dirt_cells if dirt_cells else [(1,1), (2,3), (4,4)]
        self.obstacle_cells = obstacle_cells if obstacle_cells else [(0,3), (3,1), (2,2)]
        
        # Rewards
        self.rewards = {cell: 1 for cell in self.dirt_cells}
        self.rewards.update({cell: -1 for cell in self.obstacle_cells})
        
        # Actions: up, down, left, right
        self.actions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    def reset(self):
        self.state = self.start
        return self.state
    
    def step(self, action):
        """Take an action and return next_state, reward, done"""
        x, y = self.state
        dx, dy = action
        new_state = (x+dx, y+dy)
        
        # Stay within bounds
        if 0 <= new_state[0] < self.size and 0 <= new_state[1] < self.size:
            self.state = new_state
        else:
            new_state = self.state  # invalid move, stay put
        
        reward = self.rewards.get(new_state, 0)
        done = len(self.dirt_cells) == 0  # finished when all dirt cleaned
        
        # If dirt cleaned, remove it
        if new_state in self.dirt_cells:
            self.dirt_cells.remove(new_state)
        
        return new_state, reward, done
    
    def available_actions(self):
        return self.actions


def random_policy(env, episodes=1):
    """Robot moves randomly"""
    for ep in range(episodes):
        state = env.reset()
        total_reward = 0
        steps = 0
        while True:
            action = random.choice(env.available_actions())
            next_state, reward, done = env.step(action)
            total_reward += reward
            steps += 1
            if done or steps > 50:  # limit steps
                break
        print(f"Episode {ep+1}: Total Reward={total_reward}, Steps={steps}")


def greedy_policy(env, episodes=1):
    """Robot moves greedily toward nearest dirt"""
    for ep in range(episodes):
        state = env.reset()
        total_reward = 0
        steps = 0
        while True:
            if env.dirt_cells:
                # Move toward nearest dirt
                dirt = min(env.dirt_cells, key=lambda d: abs(d[0]-state[0]) + abs(d[1]-state[1]))
                dx = np.sign(dirt[0]-state[0])
                dy = np.sign(dirt[1]-state[1])
                action = (dx, dy) if (dx, dy) in env.available_actions() else random.choice(env.available_actions())
            else:
                action = random.choice(env.available_actions())
            
            next_state, reward, done = env.step(action)
            state = next_state
            total_reward += reward
            steps += 1
            if done or steps > 50:
                break
        print(f"Episode {ep+1}: Total Reward={total_reward}, Steps={steps}")


# Run simulation
env = GridMDP()
print("Random Policy Simulation:")
random_policy(env, episodes=3)

env = GridMDP()
print("\nGreedy Policy Simulation:")
greedy_policy(env, episodes=3)