#Operations on Strings

a = "IEEE"
b = "PESIT"
c = "Student Branch"
d = str(2014)

#Concatenation
con1 = (a+b+c)
con2 = (a+" "+b+" "+c)
con3 = a + d

#Length of a String
length = len(con1)

#Index
index = c.index("u")

#Count
count = a.count("E")
count1 = a.count("e")

#Slicing
slice = c[3:10]

#Spliting
split = c.split(" ")

#Replace
replace = c.replace("Branch","Community")

#Finding
find = c.find("e")

#Repeat
repeat = "IEEE " * 4

#Position
position1 = c[3]
position2 = c[:5]
position3 = c[5:]
position4 = c[-5:]
position5 = c[:]
position6 = c[0:14:2]

#String Formatiing
sf1 = "String"
sf2 = "Format"

sf = "This is a %s and this is how we %s it"%(sf1,sf2)
