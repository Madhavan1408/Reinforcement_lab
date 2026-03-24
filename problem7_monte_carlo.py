import random

def simulate_episode():
    rewards = []
    for _ in range(10):
        rewards.append(random.choice([1, -1]))
    return sum(rewards)

returns = [simulate_episode() for _ in range(1000)]
print("Estimated Value:", sum(returns)/len(returns))
