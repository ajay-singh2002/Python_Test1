# enumerate function
# method - 1
lists = [22,45,32,55]
x = 0
for i in lists:
    print(x,i)
    x += 1

# method - 2
lists = [22,45,32,55]
for i in range(len(lists)):
    print( i,lists[i])

# for using enumerate function
lists = [22,45,32,55]
for i in enumerate(lists):
    print(i)
