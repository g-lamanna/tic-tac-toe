#==========================================================
#=====================TIC=TAC=TOE==========================
#==========================================================

import random 
import time

#Map out board location pairs to be mutated by players
board_places = {
  '1':1,
  '2':2,
  '3':3,
  '4':4,
  '5':5,
  '6':6,
  '7':7,
  '8':8,
  '9':9
}

#Show playing board
def board():
  print(f'\n\t\t{board_places["1"]}|{board_places["2"]}|{board_places["3"]}')
  print('\t\t-----')
  print(f'\t\t{board_places["4"]}|{board_places["5"]}|{board_places["6"]}')
  print('\t\t-----')
  print(f'\t\t{board_places["7"]}|{board_places["8"]}|{board_places["9"]}')

  # 1|2|3
	# -----
	# 4|5|6
	# -----
	# 7|8|9


#Checks board to see if winning conditions are met 
def win_checker():
  #2-D array of winning combinations
  winning_combinations = [
    [board_places["1"],board_places["2"],board_places["3"]],
    [board_places["4"],board_places["5"],board_places["6"]],
    [board_places["7"],board_places["8"],board_places["9"]],
    [board_places["1"],board_places["4"],board_places["7"]],
    [board_places["2"],board_places["5"],board_places["8"]],
    [board_places["3"],board_places["6"],board_places["9"]],
    [board_places["1"],board_places["5"],board_places["9"]],
    [board_places["3"],board_places["5"],board_places["7"]]
  ]

  #loops through to check if every element is the same the first element in the list
  for combo in winning_combinations:
    for j in combo:
      if all(j == combo[0] for j in combo):
        return True
  return False


#Main game function
def game():
  print(f"\t**********************")
  print(f"\tWELCOME TO TIC TAC TOE")
  print(f"\t**********************\n")
  
  #To loop continously until player picks one of the presented choices
  while True:
    user_pick = input(f"\tPLEASE PICK YOUR GAME CHARACTER: 'X' or 'O' ")
    
    #Assigns user, game character
    if user_pick == "X":
      user_char = user_pick
      cpu_char = 'O'
      break

    elif user_pick == "O":
      user_char = user_pick
      cpu_char = "X"
      break

    #Error check, loops back to the top
    else:
      print(f"\n\t{user_pick} is an invalid character, please pick again\n")

  print(f"\n\tUser => {user_char} \n \tCPU => {cpu_char}\n")

  player_chars = [user_char,cpu_char]

  #Assign first move randomly
  if random.choice(player_chars) == user_char:
    print(f"\tYou go first!")
    board()

    #Checking if winning combination is hit
    while not win_checker():
      #Allows players to make moves and verify if winning combination returns True
      if user_move(user_char):
        break;
      elif cpu_move(cpu_char):
        break;
  else:
    print(f"\tCPU goes first...")
    time.sleep(3)

    #Checking if winning combination is hit
    while win_checker() is False:
     
      #Allows players to make moves and verify if winning combination returns True
      if cpu_move(cpu_char):
        break;
      elif user_move(user_char):
        board()
        break;



def cpu_move(cpu_char):
  #Randomizes computer move
  cpu_choice = str(random.randint(1,9))

  #loops through board to check if choice is in .value()
  for key in board_places:
    if cpu_choice == key:
      #Checks if current value is a game character
      if board_places[key] == 'X' or board_places[key] == 'O':
        #makes player pick again
        cpu_move(cpu_char)
      else:
        #Assigns game character as value to chosen key
        board_places[key] = cpu_char
        board()
        break
  
  #Checks board if winning combination is met
  if win_checker():
    print("\tComputer wins...\n")
    return True



def user_move(user_char):
  #Takes user input
  user_choice = input('\n\tChoose a spot: ')
  
  #loops through board to check if choice is in .value()
  for key in board_places:
    if user_choice == key:
      #Checks if current value is a game character
      if board_places[key] == 'X' or board_places[key] == 'O':
        print(f'\tInvalid move')
        #makes player pick again
        user_move(user_char)
      else:
        board_places[key] = user_char
        break

  #Checks board if winning combination is met
  if win_checker():
    board()
    print('\tYou won!\n')
    return True


def main():
  game()

if __name__ == '__main__':
  main()