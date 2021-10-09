import random 
print("Number Guessing Game")
rand=random.randint(1,20)
print("Guess a Number between 1-20")

chances=0
while(chances<5):
    chances=chances+1
    guess=int(input("Enter Your Guess"))
    if(guess==rand):
       print("Congratulations You Won!!")
       break
    elif(guess<rand):
        print("Guess a number higher")
    else:
        print("Guess a number lesser")
if not chances<5:
    print("You Loose")