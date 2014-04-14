#Combining Functions with Loops for better code

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

#create a list of these functions

operations = [add,sub,mul,div]

#Perform all operations on given numbers
a=5
b=3
for func in operations:
    print func(a,b)
