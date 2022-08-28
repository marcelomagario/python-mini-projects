# PRIZE DRAW PROGRAM
# The user will define the number of participants and register their name
# The program will show the name of all participants
# The program will generate a randon winner and show on screen.
# Author: Marcelo Magario

import random
participants_names = []
number_participants = int(input('Please, tell me how many participants: '))
for i in range(1, number_participants + 1):
    new_participant = str(input(f'Name of participant {i}: '))
    participants_names.append(new_participant)
# Pick random participant
winner = random.choice(participants_names)
print(f'Number of participants: {number_participants}')
print(f'Participants names: {participants_names}')
print(f'The winner is: *** {winner} ***')
