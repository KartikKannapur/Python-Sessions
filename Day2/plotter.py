#Demo of Matplotlib
#Requires six,python-dateutil & pyparsing libraries as well

import matplotlib.pyplot as p
import math as m
xrang=500
smooth=4.0
list1=[]
sin=[]
for i in range(0,2000):
    list1.append(i/smooth)
for i in list1 :
    sin.append(m.sin(i))

p.plot(sin)
p.axis([0,xrang,-1,1])
p.xlabel('x')
p.ylabel('sin(x)')
p.show()
