# Rock Paper and Scissor game made in Python
# Author: Marcelo Magario
# Date: 28/08/2022

import random

# Player choose Rock, Paper or Scissor
valid_choice = ['rock', 'paper', 'scissor']
player_choice = str(input('Choose your hand (Rock, Paper or Scissor): ')).lower()
if player_choice not in valid_choice:
    result = f'This "{player_choice}" is invalid. Please choose one of the options: {valid_choice} '
else:
    computer_choice = random.choice(valid_choice)
    result = f'Computer hand: {computer_choice}'
    if player_choice == computer_choice:
        result = f'Draw! Your choice "{player_choice}" is same as your oponent. '
    elif (player_choice == 'rock' and computer_choice == 'scissor') or (player_choice == 'paper' and computer_choice == 'rock'):
        result = f'{player_choice} beats {computer_choice}! You won!'
    else:
        result = f'{player_choice} loose to {computer_choice}! You lost'
print(result)
