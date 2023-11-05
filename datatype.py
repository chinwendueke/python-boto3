#numbers (integer, float, complex numbers)

#Interger
a = 3
b =-3
c = 3.1
d = 3+5j
print (type(a))
print (type(b))
print (type(c))
print (type(d))

#String
Name = "Amarachi"
classes ="march2023"
print(type(Name))
print(type(classes))
p = "I love to code in python"
s = "Amarachi Eke"


#string methods
print(Name.lower())
name_upper = Name.upper()
name_tittle = Name.title()
print(name_upper)
print(name_tittle)
print(s.title())
print(Name.isdigit())
print(Name.isalpha())    #meanins it's alphabetical?
print(classes.isdigit()) #meaning it's a digit?
print(classes.isalnum()) #meaning it's alpha-numeric?
#print(help(str)) - to get string help

#Lenght of variable
print(len(Name))

#strip function --- to remove extra spaces around your data
name2= Name.strip() #this will clean any extra spaces added to Amarachi

p = "python"
print(p[0])
print(p[-1]) #meaning last letter or print from the last letter
print(p[0:3])

#Boolean #
is_student = True
is_cloud = False

