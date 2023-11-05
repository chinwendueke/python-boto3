"""import time

while True: #used for an infinite condition until the condition is met or server is broken
    time.sleep(3)""" #means will sleep 3 seconds

good_guess=10
number_of_trials = 0


while number_of_trials <= 2:
    number_of_trials+=1
    try:
        choice = int(input("Please enter a number between 1 and 20: "))
        if number_of_trials == 3:
            print("sorry, you lost. Try again")
        if choice not in range(1,21):
            print("invalid entry")  
        elif choice == good_guess:
            print("Good job, you won!!!")
            break # to stop a loop, use break
        elif choice < good_guess:
            print("sorry, your number is lower")
        elif choice > good_guess:
            print("sorry your number is bigger")
    except:
        print("Something went wrong, please input a number not a letter")


