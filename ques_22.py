# Use len() and enumerate() to print index and value of a list
# using len()
x = ['village', 'town', 'city', 'country']

for i in range(len(x)):
    print(i, x[i])

# using enumerate()
x = ['village', 'town', 'city', 'country']

for index,value in enumerate(x):
    print(index,value)

