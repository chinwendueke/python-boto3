# Try and Error ---error handling in python

try:
    print(a) # "a" is not declared as a variable and would throw an error
except:
    print("something wrong! please try again")

print("hello")

#Also
try:
    print(a)
except Exception as e:
    print(e)
else:
    print("boom")

print("hello")

#

try:
    num =int(input("Please enter a number: "))
    print(num)
except Exception as e:
    print(e)

#
try:
    num =int(input("Please enter a number: "))
    print(num)
except:
    print("something went wrong, please try again")