import random

def play():
    user = input("Please type 'r' for Rock, 'p' for Paper or 's' for Scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie!'
    
    if user == '':
         return 'Please enter something.'

    # Rules of the game. r > s, s > p, p > r

    if is_win(user,computer):
        return 'You won!!'
    
    return 'You lost :('

def is_win(player, opponent):
        # will return true if player wins

        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True

print(play())