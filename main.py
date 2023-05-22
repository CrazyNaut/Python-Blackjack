import random

# Dictionary containing all card totals
card_dict = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}

# Player class
# This will control all operations relating to player actions
class Player:
    def __init__(self, player):
        self.player = player
        self.cards = []
        self.total = 0
    
    # Determines whether to end the game
    def check_total(self):
        print("You now have {} points.".format(self.total))
        if self.total == 21:
            print("BLACKJACK!")
            return False
        if self.total > 21:
            print("BUST!\nSorry, better luck next time!")
            return True
        else:
            return False

    # If "Hit" is selected
    def add_card(self):
        print("Selecting a card...")
        face, value = random.choice(list(card_dict.items()))
        print("You drew a {}!".format(face))
        
        # If the card drawn is an ace, the user will be able to select whether to add 1 or 11 points
        if face == 'A':
            done = False
            while not done:
                ace = input("How many points would you like to add?\nCurrent score: {}\n1) 1\n2) 11\n".format(self.total))
                if not ace.isnumeric():
                    print("Invalid input. Please try again.\n")
                elif int(ace) < 1 or int(ace) > 2:
                    print("Invalid input. Please try again.\n")
                elif int(ace) == 1:
                    print("Adding 1 point...")
                    self.total += 1
                    done = True
                elif int(ace) == 2:
                    print("Adding 11 points...")
                    self.total += 11
                    done = True
        else:
            print("Adding {} points...".format(value))
            self.total += value

        self.cards.append(face)
        
    
    # If "View hand" is selected
    def view_hand(self):
        if len(self.cards) == 0:
            statement = "Your hand is currently empty."
        else:
            statement = "Your hand is as follows:\n"
            for card in self.cards:
                statement += str(card) + " "
        statement += "\nTotal: {}\n".format(self.total)
        print(statement)
        self.check_total()


# Program starts here

print("===================\n")
print("     BLACKJACK     \n")
print("===================\n\n")

# First prompt
ready = False
while not ready:
    num = input("How many people will be playing? (1-4): ")
    if not num.isnumeric():
        print("Invalid input. Please try again.\n")
    elif int(num) < 1 or int(num) > 4:
        print("Invalid input. Please try again.\n")
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

# Main gameplay
# Each player will be given this prompt until they bust or stay
for entrant in players:
    bust = False
    print("\nPlayer {}\'s turn!".format(entrant.player))
    while not bust:
        choice = input("\nWhat would you like to do?\n1) Hit\n2) Stay\n3) View hand\n")
        if not choice.isnumeric():
            print("Invalid input. Please try again.")
            continue
        elif int(choice) < 1 or int(choice) > 3:
            print("Invalid input. Please try again.")
            continue
        elif int(choice) == 1:
            entrant.add_card()
            bust = entrant.check_total()
        elif int(choice) == 2:
            print("You have chosen to stay with {} points.\n".format(entrant.total))
            break
        elif int(choice) == 3:
            entrant.view_hand()
            continue

# Calculate and display final results
totals = []
print("\nFinal results\n")
for entrant in players:
    if entrant.total == 21:
        result = "(BLACKJACK)"
        totals.append(entrant.total)
    elif entrant.total > 21:
        result = "(BUST)"
        totals.append(0)
    else:
        result = ""
        totals.append(entrant.total)
    print("Player {} total: {} {}\n".format(entrant.player, entrant.total, result))

# Determine the winner based on point totals
if len(players) > 1:
    if totals.count(max(totals)) == 1:
        print("Player {} wins!\n\n".format(totals.index(max(totals)) + 1))
    else:
        print("It's a tie!\n\n")


print("Thank you for playing!\n")