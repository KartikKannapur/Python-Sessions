#Demo on Functions in Python

value=5
#Functions that don't take or return a value
def myfunc():
    print 'Hello World';

#Functions that take a value, but don't return one
def myfunc2(a):
    print a;

#Functions that don't take a value, but return one
def myfunc3():
    return value;

#Functions that take a value and return one
def myfunc4(a,b):
    c=a+b;
    return c;

# Calling Functions within Functions
def square(x):
	sq = (x*x)
	return sq

def cube(x):
	cu = (square(x)*x)
	return cu



