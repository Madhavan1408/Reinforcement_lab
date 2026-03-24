import numpy as np

def generate_data(n=100):
    demand = np.random.randint(10, 50, n)
    price = np.random.uniform(5, 20, n)
    sales = demand - price + np.random.randn(n)*2
    return demand, price, sales

demand, price, sales = generate_data()
print("Sample Demand:", demand[:5])
