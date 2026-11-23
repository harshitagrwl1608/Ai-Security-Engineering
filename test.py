import random
data=['Amit','Rahul','Priya','Neha','Raj']

random.seed(10)
for i in data:
    print(random.choice(data))