# Random Number Generator
import random
l = random.randint(1,10)
v = input("Guess the number")
lp = int(v)
x = True
while(x == True):
    if(lp > l):
        print("Too high")
    if(lp < l):
        print("Too low")
    if(lp == l):
        print("You guessed the number!")
