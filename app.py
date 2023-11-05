_app1 = input("Please key in your username: ")
_pass = input("what is your password: ")
_login = _app1 + _pass
#_app1 = "admin"
#_pass = "admin"
#print(_app1)
#print(_pass)
print(_login.strip())
if _login == 'admin': 
   print("Successfully logged in")
#if _pass == 'admin':
#   print("Successfully logged in")
else:
   print("wrong username or password")
