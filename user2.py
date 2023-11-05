_user2 = input("what is your middle name please: ")
_len = len(_user2.strip())
print(_len)
if _len < 4:
    print("invalid entry")
if _len > 4:
    print("valid entry")