#How to created a derived class
#Here drclass() is derived from myclass defined in the classes.py example
#Same rules apply here as well
#Eg. of usage - a=drclass()

from classes import myclass

class drclass(myclass):
    def surname(self,name):
        global sur
        sur=str(name)
    def printsur(self):
        print sur
