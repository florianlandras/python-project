import random

def get_choices():
  player_choice = input("Enter a choice (rock,paper,scissors: ")
  options = ["rock", "paper", "scissors"]

  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, Computer choice {computer}")
  if player == computer:
    return "It's a tie!" 
  if player =="rock" and computer == "scissors":
    return "Rock smashes scissors! You win!"
  if computer == "scissors" and player == "rock":
    return "Rock smashes scissors! You lose!"
  elif player == "paper":
    if computer == "rock":
      return "Paper covers rock! You win"
  else:
    return "Scissor cuts paper. You lose!" 



check_win("rock", "paper") 
          




