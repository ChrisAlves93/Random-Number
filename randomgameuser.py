import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Could also be high b/c low = high
            guess = high
        feedback = input(f'Is {guess} too high(H), too low(L), or correct(C)????: ').lower()
        if feedback == 'h':
            high = guess - 1
            try:
                high = guess + 1
            except:
                print('Error in the system. Report bug!!!')
        elif feedback == 'l':
            low == guess + 1
    print(f'The computer guessed your number, {guess}, correctly!!!')

computer_guess(10)