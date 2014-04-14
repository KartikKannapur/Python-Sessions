#User defined module contained custom functions
#Create a custom module by typing functions as below
#The module can then be imported with - import modulename
#Then, to use a function within the module - modulename.functionname()


#Number of times number s appears in n
def search(s,n):
    count=0
    a=[]
    while n!=0:
        rem=n%10
        a.append(rem)
        n=n/10
    l=len(a)
    for i in range(l):
        if a[i]==s:
            count+=1
        i+=1
    return count


#Prints all factors of number n
def factors(n):
    a=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
        i+=1
    return a


#Checks if number n is prime or not
def isprime(n):
    i=2
    flag=1
    while i<n:
        if n%i==0:
            flag=0
        i+=1
    if flag==1:
        return 1
    else:
        return 0

#Finds sum of all digits in a number
def numsum(n):
    sum1=0
    l=len(str(n))
    for i in range(l):
        sum1+=n%10
        n=n/10
        i+=1
    return sum1
    
        
    
    
