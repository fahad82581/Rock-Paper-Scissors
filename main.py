import random
def comp():
  list = ["rock", "paper", "scissors"]
  computer = random.choice(list)
  return computer.lower()

def user():
  choice = input("Enter a choice (rock, paper, scissors): ")
  return choice.lower()

def check(choice, computer):
  print(f"if you chose {choice}, computer chose {computer}")
  if choice == computer:
    print("It's a tie!")
  elif choice == "rock":
    if computer == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("Paper covers rock! You lose.")

  elif choice == "paper":
    if computer == "rock":
      print("Paper covers rock! You win!")
    else:
      print("Scissors cuts paper! You lose.")

  elif choice == "scissors":
    if computer == "paper":
      print("Scissors cuts paper! You win!")
    else:
      print("Rock smashes scissors! You lose.")

check(user(), comp())
