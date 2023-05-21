import random

card_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

class Player:
    def __init__(self, player):
        self.player = player
        self.cards = {}
        self.total = 0
    
    def add_card():
        pass



print("===================\n")
print("     BLACKJACK     \n")
print("===================\n\n")

# First prompt
ready = False
while not ready:
    num = input("How many people will be playing? (1-4): ")
    if not num.isnumeric():
        print("Invalid input. Please try again.")
    elif int(num) < 1 or int(num) > 4:
        print("Invalid input. Please try again.")
    else:
        ready = True

# Initialize player list
players = []
player1 = Player(1)
players.append(player1)
if int(num) > 1:
    player2 = Player(2)
    players.append(player2)
if int(num) > 2:
    player3 = Player(3)
    players.append(player3)
if int(num) > 3:
    player4 = Player(4)
    players.append(player4)

for entrant in players:
    print("Player {}\'s turn!".format(entrant.player))
    while entrant.total <= 21:
        choice = input("What would you like to do?\n1) Hit\n2) Stay\n3) Fold\n")
        if not choice.isnumeric():
            print("Invalid input. Please try again.")
            continue
        elif int(choice) < 1 or int(choice) > 3:
            print("Invalid input. Please try again.")
            continue
        elif int(choice) == 1:
            pass
        elif int(choice) == 2:
            pass
        elif int(choice) == 3:
            pass