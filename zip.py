fruits = ['apple', 'banana', 'cherry']
colors = ['red', 'yellow', 'red']

# zip combines to iterables into one

for fruit, color in zip(fruits, colors):
    print(f"Fruit {fruit}   Color: {color}")