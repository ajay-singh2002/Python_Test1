                           # functions
# average of 3 numbers
def average(a,b,c):
    sum = a+b+c
    average = sum/3
    print(average)

average(33,54,33)

# return keyword = return keyword ka use krte h hum to call krte time new variable me lete h
def average(a,b,c):
    sum = a+b+c
    average = sum/3
    return average

a = average(33,54,33)
print(a)
b = average(33,54,33)
print(b)

def greet(name):
    print("Hello")

greet()