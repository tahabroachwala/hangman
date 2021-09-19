# The Guess Game   

# secret number between 1 and 100 
import random
randomNumber = random.randrange(1, 100)  # changed from 10 to 100
#print randomNumber #check if it's working

# rules
print('Hello and welcome to the guess game !')
print('The number is between 1 and 100')

guesses = set()  # your set of guesses
guessed = False
tries = 0        # no need add 1 to the tries here

while guessed == False:

    userInput = int(input("Please enter your guess: "))

    if userInput not in guesses:   # if it's not in our set
        tries += 1                 # increase the tries
        guesses.add(userInput)     # add it to our set

    if userInput == randomNumber:
        guessed = True
        tries = str(tries)
        print("Congratulations ! You win after " + tries + " tries ! ")

    elif userInput > 100 or userInput < 1:
        print("The guess range is between 1 and 100, please try again")

    elif userInput > randomNumber:
        print("Your guess is too large")

    elif userInput < randomNumber:
        print("Your guess is too small")

print("End of the game, please play again")
