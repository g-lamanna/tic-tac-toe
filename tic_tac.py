import random 
import time

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
def board():
  print(f'\t{board_places["1"]}|{board_places["2"]}|{board_places["3"]}')
  print('\t-----')
  print(f'\t{board_places["4"]}|{board_places["5"]}|{board_places["6"]}')
  print('\t-----')
  print(f'\t{board_places["7"]}|{board_places["8"]}|{board_places["9"]}')

  # 1|2|3
	# -----
	# 4|5|6
	# -----
	# 7|8|9
def win_checker():
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

  for combo in winning_combinations:
    for j in combo:
      if all(j == combo[0] for j in combo):
        return True
  return False
def cpu_move(cpu_char):
  cpu_choice = str(random.randint(1,10))
  print(f"\tcomputer chose {cpu_choice}")
  for key in board_places:
    if cpu_choice == key:
      if board_places[key] == 'X' or board_places[key] == 'O':
        print(f'\tInvalid move')
        cpu_move(cpu_char)
      else:
        board_places[key] = cpu_char
        break
  if win_checker():
    board()
    print("\tComputer wins...")
    return True
def user_move(user_char):
  user_choice = input('\n\tChoose a spot: ')
  for key in board_places:
    if user_choice == key:
      if board_places[key] == 'X' or board_places[key] == 'O':
        print(f'\tInvalid move')
        user_move(user_char)
      else:
        board_places[key] = user_char
        break
  if win_checker():
    board()
    print('\tYou won!')
    return True

def game():
  print(f"\t**********************")
  print(f"\tWELCOME TO TIC TAC TOE")
  print(f"\t**********************\n")
  
  while True:
    user_pick = input(f"\tPLEASE PICK YOUR GAME CHARACTER: 'X' or 'O' ")

    if user_pick == "X":
      user_char = user_pick
      cpu_char = 'O'
      break
    elif user_pick == "O":
      user_char = user_pick
      cpu_char = "X"
      break
    else:
      print(f"\n\t{user_pick} is an invalid character, please pick again\n")

  print(f"\n\tUser => {user_char} \n \tCPU => {cpu_char}\n")
  
  player_chars = [user_char,cpu_char]
  if random.choice(player_chars) == user_char:
    print(f"\tYou go first!")
    while win_checker() is False:
      board()
      if user_move(user_char):
        break
      elif cpu_move(cpu_char):
        break
     
      

  else:
    print(f"\tCPU goes first...")
    time.sleep(3)
    while win_checker() is False:
      board()
      if cpu_move(cpu_char):
        break
      elif user_move(user_char):
        break;
         
game()