"""
Loops
"""


# import
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# generate random number range 1-10
number = random.randint(1,10)

#print(number)


# control
isGuessRight = False

# loop while
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    # condicional
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


# loop for
for x in range (0, 11):
    print(x)


