class Player:
    pass

print("===================\n")
print("     BLACKJACK     \n")
print("===================\n\n")

ready = False
while not ready:
    players = input("How many people will be playing? (1-4): ")
    if int(players) < 1 or int(players) > 4:
        print("Please try again.")
    else:
        ready = True

player1 = Player()
if players > 1:
    player2 = Player()
if players > 2:
    player3 = Player()
if players > 3:
    player4 = Player()