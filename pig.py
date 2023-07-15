#THIS IS NOT MADE BY MYSELF, I JUST DID SOME MODIFICATIONS TO LEARN!!!
import random 

#Function of roll
def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value,max_value)

    return roll

#Forever loop as long as it's false
while True: 
    players = input("Enter the number or players (2 - 4): ")
    #checking whether players is a digit or not
    if players.isdigit():
        #convert players into int
        players = int(players)
        #checking whether players is between 2 - 4
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    #if players is not an int 
    else:
        print("Invalid, try again.")

max_scores = 50
#counting the amount of players that currently playing
player_scores = [0 for _ in range(players)]

#forever loop until score reaches the max_scores
while max(player_scores) < max_scores:
    #this is for the turn of each players 
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your current score is:", player_scores[player_idx], "\n")

        current_score = 0

        should_roll = input("Would you like to try again? (y)")
        #checking whether should_roll is not letter "y" if not, then break.
        if should_roll.lower() != "y":
            break 
        #basically the same as else, the function will just repeat
        value = roll()
        #checking whether value is 1 or not
        if value == 1:
            print("You rolled a 1! Turn done")
            current_score = 0
            break
        #adding the score that each player get to current_score
        else:
            current_score += value
            print("You rolled a:", value)

        print("Your score is", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_scores = max(player_scores)
winning_idx = player_scores.index(max_scores)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_scores)
