import time
import os
from collections import deque
import Game
from Player import Player
import copy

def main():

    Game.welcome()
    time.sleep(2)
    play_again = True
    players_names = Game.choose_players_names()
    player1 = Player(name=players_names[0], symbol="X")
    player2 = Player(name=players_names[1], symbol="O")
    global_first_hand = deque([player1, player2])
    while play_again:
        current_hand = copy.deepcopy(global_first_hand)
        made_turns = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        steps = 0
        while True:
            os.system('cls')
            Game.draw_table(made_turns)
            Game.make_turn(made_turns=made_turns, player=current_hand[0])
            if not Game.check_win_conditions(made_turns, current_hand[0]):
                current_hand.rotate()
            else:
                os.system('cls')
                Game.draw_table(made_turns)
                Game.player_win_round(current_hand[0])
                for player in global_first_hand:
                    if current_hand[0].name == player.name:
                        player.add_wins_number()
                current_hand[0].add_wins_number()
                break
            steps += 1
            if steps == 9:
                os.system('cls')
                Game.draw_table(made_turns)
                print("Nobody won the round. It is Draw!\n")
                break
        if not Game.play_again():
            break
        else:
            global_first_hand[0].change_symbol()
            global_first_hand[1].change_symbol()
            global_first_hand.rotate()
            Game.what_symbol_players_have(global_first_hand)
    Game.who_is_final_winner(player1, player2)
    Game.goodbye()

if __name__ == "__main__":

    try:
        main()
    except Exception as ex:
        print(f"The following problem happened in the program:  {ex}")
        print("The program will be terminated in 10 seconds")
        time.sleep(10)
