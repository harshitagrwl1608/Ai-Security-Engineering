import random

data = ["Amit", "Rahul", "Priya", "Neha", "Raj"]

random.seed(10)

for _ in range(5):
    print(random.choice(data))
