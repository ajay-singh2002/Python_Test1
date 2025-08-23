# (Loops) Count how many even numbers are in a list.
num = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in num:
    if i %2==0:
        count += 1

print("total number of even",count)