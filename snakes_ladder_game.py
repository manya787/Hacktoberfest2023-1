import random

# Initialize player positions
player1_pos = 1
player2_pos = 1

# Define the snakes and ladders on the board
snakes_and_ladders = {3: 22, 11: 26, 17: 19, 19: 8, 21: 9, 27: 1, 20: 29}

# Function to roll a die
def roll_die():
    return random.randint(1, 6)

# Function to play a turn
def play_turn(player):
    input(f"Player {player}, press Enter to roll the die...")
    roll = roll_die()
    print(f"Player {player} rolled a {roll}.")
    return roll

# Main game loop
while player1_pos < 30 and player2_pos < 30:
    # Player 1's turn
    roll1 = play_turn(1)
    player1_pos += roll1
    if player1_pos in snakes_and_ladders:
        player1_pos = snakes_and_ladders[player1_pos]
    print(f"Player 1 is at position {player1_pos}")

    # Check if Player 1 has won
    if player1_pos >= 30:
        print("Player 1 has won!")
        break

    # Player 2's turn
    roll2 = play_turn(2)
    player2_pos += roll2
    if player2_pos in snakes_and_ladders:
        player2_pos = snakes_and_ladders[player2_pos]
    print(f"Player 2 is at position {player2_pos}")

    # Check if Player 2 has won
    if player2_pos >= 30:
        print("Player 2 has won!")
        break

# End of the game
print("Game over!")
