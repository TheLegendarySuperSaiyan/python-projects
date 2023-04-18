from random import randint
import time 

t = ["Paper", "Rock", "Scissor : "]
options = input("Paper,Rock,Scissor : ")

computer = t[randint(0, 2)]

if (options == "Rock" and computer == "Paper"):
  time.sleep(1)
  print('computer chose Paper')
  print("Player Wins")

elif (options == "Rock" and computer == "Scissor"):
  time.sleep(1)
  print('computer chose Scissor')
  print("Computer Wins")

elif (options == "Rock" and computer == "Rock"):
  time.sleep(1)
  print('computer chose Rock')
  print("It's a tie")

elif (options == "Paper" and computer == "Scissor"):
  time.sleep(1)
  print('computer chose Scissor')
  print("Computer wins")

elif (options == "Paper" and computer == "Rock"):
  time.sleep(1)
  print('computer chose Rock')
  print("Player won")

elif (options == "Paper" and computer == "Paper"):
  time.sleep(1)
  print('computer chose Paper')
  print("It's a tie")

elif (options == "Scissor" and computer == "Scissor"):
  time.sleep(1)
  print('computer chose Scissor')
  print("It's a tie")

elif (options == "Scissor" and computer == "Rock"):
  time.sleep(1)
  print('computer chose Rock')
  print("Computer wins")

elif (options == "Scissor" and computer == "Paper"):
  time.sleep(1)
  print('computer chose Paper')
  print("Player wins")
