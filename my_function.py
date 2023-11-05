

def hello():  # To decleare Function, we start with 'def'.we just declared the function hello here.
    print("hello world")
hello()  #This is how a function is called

def hello1(name):
    print(f"hello {name}")  #
hello1('Amara')

def Command(cmd):
    import os
    os.system(cmd)
Command('dir')

def StringLen():
    pass    # means, do nothing. also used to bypass coding at a point so you can come back to it later

def addition(a,b,c):
    print(a+b+c)
addition(5,3,5)

#Also
def addition(a,b):
    return a+b
a=addition(5,5)
print(a)