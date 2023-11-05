#for loop - you loop through a list of somethin (eg) looping thru a list of users to see when the were created to know which ones to delete
for i in (3,4,5,7,8,9,12):   #"i" as in item
    print(i)

#Also
for i in range(20):
    print(i)

#Also
for i in ['aws','python','powershell','github']:
    print(i)

#Also
for i in range(1,20): #meaning 1 to 20
    if i%2 ==0:  # % means divide; meaning if "i" is divisible by 2
        print(i)

#Also
divisibleby2=[]
for i in range(1,20):
    if i%2 ==0:
        divisibleby2.append(i)
print(divisibleby2)
print(len(divisibleby2))