#How to define a class in Python, containing certain variables and methods
#A variable can be made available to all methods in the class.
#Such a variable has to be declared as 'global' within every method that uses it
#'self' must be used as a default argument when defining a method in a class

class myclass:
    
    def modage(self,num):
        global ag
        ag=num
        print str(i)
    def name(self,name):
        global inputname
        inputname=str(name)
    def dob(self,date):
        global dob1
        dob1=str(date)
    def age(self,age1):
        global ag
        ag=str(age1)
    def getdetails(self):
        print inputname+'\n'+dob1+'\n'+ag
