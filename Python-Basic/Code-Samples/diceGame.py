import random

print("Welcome to our game. Roll the dice and guess the number.")
print("If you get it correct, you get a point, and if you get it wrong,")
print(" you lose points")
      
userGuess = int(input("Enter a number between 1- 6: "))
rolledDice = random.randint(1,6)
print(userGuess, "-> user guess")
print(rolledDice, "-> rolled dice")
# First example is while loop
counter = 1
while rolledDice != userGuess:
     print(counter," -> counter")
     if counter >= 3:
          break
     print("oops, you got  it wrong!")
     userGuess = int(input("Enter a number between 1- 6: "))
     counter += 1
     
if counter < 3:
     print("Hooray, you guessed correctly")
else:
     print("Oops you got it wrong!")
     print("You used all your guesses")
     

