#NUMBER GUESSING GAME
user_input=input("whats your name?")
user_output=print("hello,",user_input,".Welcome to the game centre!")
import random
number=random.randint(1,100)
#checking the guess
guess=int(input("guess a number between 1 and 100:"))

if guess >100 or guess <1:
  print("sorry!try again")
elif guess==number:
  print("very correct ,you can go to the next level")
elif guess>number:
  print("you are good at counting ,thats good")
elif guess<number:
  print("i think you are still at primary coz you dont know big numbers")