import random

def guess(x):
    random_number = random.randint(1, x) #random.randint is utilized to return a random integer value between the two lower and higher limits
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number beteen 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Number is too low.')
        elif guess > random_number:
            print('Sorry, guess again. Number is too high')
        else:
            print(f'Congrats! You have guessed the number {random_number} correctly!')

guess(10)