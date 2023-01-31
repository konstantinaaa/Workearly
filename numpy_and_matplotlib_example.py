import numpy as np
import matplotlib.pyplot as plt

products = np.array([
    ["Apple", "Orange"],
    ["Beef", "Chicken"],
    ["Candy", "Chocolate"],
    ["Fish", "Bread"],
    ["Eggs", "Bacon"]
])

random = np.random.randint(2, size=5)
# We will create a list of random products

choices = []
counter = 0
for product in products:
    choices.append(product[random[counter]])
    counter += 1

print(choices)

# We will create randomized array full of percentages
# we also have to make sure that they add up to 100

percentages = []
for i in range(4):
    percentages.append(np.random.randint(25))
percentages.append(100-np.sum(percentages))
print(percentages)

plt.pie(percentages, labels=choices)
plt.legend(loc="lower right", ncol=1)
plt.show()