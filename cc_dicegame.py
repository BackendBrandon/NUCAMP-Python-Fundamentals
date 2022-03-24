import random
game = True


def dice_game():
    global high_score
high_score = 0

while game == True:
    print("Current High Score:", high_score)
    print("1) Roll Dice")
    print("2) Leave Game")
play = input("Enter your Choice:")

if play == "1":

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print("You roll a...", die1)
    print("You roll a...", die2)

    sum = die1 + die2
    print("You have rolled a total of:", sum)

    if sum > high_score:
        print("New high score!\n")
        high_score = sum
        
    elif play == "2":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid input.")

dice_game()
