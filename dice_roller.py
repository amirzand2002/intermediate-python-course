import random

def main():
  dice_roll= int(input('How many dice would you like to roll? '))
  dice_size = int(input('How many sides are the dice? '))
  team1 = input('What is the name of the first team? ')
  team2 = input('What is the name of the second team? ')
  dice_sum_1 = 0
  print('\n')
  for i in range(dice_roll):
    roll = random.randint(1,dice_size)
    if roll ==1:
      print(f'Team {team1} rolled a {roll} !Critical Fail')
    elif roll == dice_size:
      print(f'Team {team1}  rolled a {roll} !Critical Success')
    else:
      print(f'Team {team1}  rolled a {roll}')
    dice_sum_1 +=roll
  print(f'Team {team1} rolled a total of {dice_sum_1}')
  print('\n')
  dice_sum_2 = 0
  for i in range(dice_roll):
    roll = random.randint(1,dice_size)
    if roll ==1:
      print(f'Team {team2}  rolled a {roll} !Critical Fail')
    elif roll == dice_size:
      print(f'Team {team2} rolled a {roll} !Critical Success')
    else:
      print(f'Team {team2} rolled a {roll}')
    dice_sum_2+=roll
  print(f'Team {team2} rolled a total of {dice_sum_2}')
  print('\n')
  if dice_sum_1 > dice_sum_2:
    print(f'Team {team1} have won the game by {dice_sum_1 - dice_sum_2} different')
  elif dice_sum_1 <dice_sum_2:
    print(f'Team {team2} have won the gameby {dice_sum_2 - dice_sum_1 } different')
  else:
    print('its a draw')

if __name__== "__main__":
  main()