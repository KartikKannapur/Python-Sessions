'''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?'''

'''Logic to check for prime

To check if a number(num) is prime, take the integer of its square root(sqrt(num)) and check if it has factors
in the range 3-sqrt(num). If so it is not prime!'''

import math

pos=500
count=0 #to count primes
num=3 #We start at 3, the second prime.

while count<pos-1:  #10001-1 because 2 is excluded in prev step
    
    flag=0
    for i in range(3,int(math.sqrt(num))+1): #range(3,int(num**.5)+1) - without use of math lib
        if num%i==0:
            flag=1

    if flag==0:
        count=count+1
        
    num=num+2 #Check only odd numbers to save time

print (num-2) #Remove extra 2 added at end before while loop was broken
