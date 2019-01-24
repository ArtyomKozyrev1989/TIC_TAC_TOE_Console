import string
import time


def _normalize_name(name):
    name = name.split()
    normalized_name = ""
    for i in range(len(name)):
        if i != len(name) - 1:
            normalized_name += name[i] + " "
        else:
            normalized_name += name[i]
    return normalized_name

def _check_name_symbols(name):
    allowed_symbols = string.ascii_letters + string.digits
    for symbol in allowed_symbols:
        if symbol in name:
            return True
    return False

def _choose_player_name():
    while True:
        name = input("Please choose player name: ")
        if len(name) > 40:
            print("Player's name should be less than 40 symbols, please try again!")
        else:
            if _check_name_symbols(name):
                return _normalize_name(name)
            else:
                print("Player's name should contain digits or letters, please try again!")
                
def choose_players_names():
    player1_name = _choose_player_name()
    print(f"The First player's name is {player1_name}")
    while True:
        player2_name = _choose_player_name()
        if player1_name != player2_name:
            break
        else:
            print("Player2 can't have the same name, please choose another name")
    print(f"The Second player's name is {player2_name}\n")
    print(f"{player1_name} play X")
    print(f"{player2_name} play O\n")
    return player1_name, player2_name

def goodbye():
    print("Thank you for the game, the program will be terminated in 10 seconds")
    seconds_left = 10
    for i in range(2, 10, 2):
          time.sleep(2)
          print(f"{seconds_left - i} seconds left")
    print("See you!")
    time.sleep(2)
          
def what_symbol_players_have(current_hand):
    player1 = current_hand[0]
    player2 = current_hand[1]
    print(f"{player1.name} plays {player1.symbol}")
    print(f"{player2.name} plays {player2.symbol}")

def welcome():
    print(
        '''

        ****************************************


            WELCOME TO THE GAME TIC-TAC-TOE


        ****************************************

        ''')


def play_again():
    print("Do you want to play again?")
    while (True):
        play = input("Press Y if yes or press Enter: ")
        if play.upper() == 'Y':
            return True
        elif play.upper() == '':
            return False
        else:
            print("You put incorrect symbol. Please try again.")

def player_win_round(player):
    print(f"Congratulations to {player.name}, you won the round!")

def make_turn(player, made_turns):
    possible_turns = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    while (True):
        turn = input(f"Dear {player.name} please choose number to make turn: ")
        if turn not in possible_turns:
            print(f"Dear {player.name} please choose only digits from 1 to 9 !")
        elif made_turns[int(turn) - 1] == "X" or made_turns[int(turn) - 1] == "O":
            print(f"Dear {player.name} please choose another digit")
            print(f"Digit {turn} was already used.")
        else:
            break
    made_turns[int(turn) - 1] = player.symbol

def check_win_conditions(made_turns, player):
    win_condition = [player.symbol, player.symbol, player.symbol]
    possible_combinations = (made_turns[0:3], made_turns[3:6], made_turns[6:9],
                             made_turns[1:9:3], made_turns[2:11:3], made_turns[0:9:4],
                             made_turns[2:8:2], made_turns[0:8:3])
    if win_condition in possible_combinations:
        return True
    else:
        return False

def draw_table(made_turns=["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
    print(
        f'''

            {made_turns[0]}  |  {made_turns[1]}  |  {made_turns[2]}


            {made_turns[3]}  |  {made_turns[4]}  |  {made_turns[5]}


            {made_turns[6]}  |  {made_turns[7]}  |  {made_turns[8]}


        ''')

def who_is_final_winner(player1, player2):
    print(f"{player1.name} has {player1.wins_number} victories")
    print(f"{player2.name} has {player2.wins_number} victories")
    if player1.wins_number > player2.wins_number:
        print(f"{player1.name} won the game, congratulations!")
    elif player1.wins_number < player2.wins_number:
        print(f"{player2.name} won the game, congratulations!")
    else:
        print("It seems that we have DRAW in this series")
