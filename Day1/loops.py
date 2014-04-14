#Demo for using loops in Python
#Contains demos of - for, while,break, continue, try

a=["python", "guido van rossum", "ubuntu", "linux"]

c=[1,2,44,55,4,7,82,9]

#For using range()
def for1():
    for j in range(5):
        print 'Hello World!';

        
#For using range() and len()            
def for2():
    for i in range(len(a)):
                print a[i];

#While loop

def while1():
    d=0
    while d!=10:
        print d;
        d+=1;

#break statement demo
def brk():
    for i in range(len(c)):
            if c[i]/10!=0:
                    print c[i];
                    break;
	
#Continue statement demo


def cont():
    for i in range(len(c)):
            if c[i]/10!=0:
                    print c[i];
                    continue;

#Try statement demo

def trydemo(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print 'Divide by Zero not allowed'
    else:
        print 'The result is', result
    finally:
        print 'Try Demo Complete!'
    


