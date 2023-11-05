import my_function
my_function.Command('dir')

#Also
import user as u #renaming user to u
print(u.print(_len))

#
from my_function import Command,hello #better for work env, calling only the functions you need
from my_function import * # meaning import everything in that file(not good in enterprise env)
from os import system
system('clear')

Command('ls')
hello()
hello1()


