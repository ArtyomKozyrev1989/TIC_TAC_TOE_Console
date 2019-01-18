class Player:

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins_number = 0

    def add_wins_number(self):
        self.wins_number += 1

    def change_symbol(self):
        if self.symbol == "X":
            self.symbol = "O"
        else:
            self.symbol = "X"
