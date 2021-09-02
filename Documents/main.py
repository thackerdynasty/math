import random
name = input("Hello! What is your name?")
numtoguess = random.randint(1,20)
usernum = int(input("Well, {}, I am thinking of a number between 1 and 20. What is the number you would like to guess?".format(name)))
def again():
    global usernum
    usernum = int(input(""))
    check_ans()
def check_ans():
    if usernum == numtoguess:
        print("You guessed it!")
    elif usernum < numtoguess:
        print("Your guess was too low.")
        again()
    else:
        print("Your guess was too high.")
        again()
check_ans()
