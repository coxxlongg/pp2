import random 
def numberGuess():
    print ('Hello! What is your name?')
    name = input()
    print ('Well,', name, ', I am thinking of a number between 1 and 20.')

    number = random.randint(1,20)
    guesses = 0
    
    while True:
        print ('take a guess.')
        guess = int(input())
        guesses += 1

        if guess < number:
            print ('Your guess is too low.')
        elif guess > number:
            print ('Your guess is too high.')
        else:
            print ('Good job', name, '! You guessed my number in', guesses, 'guesses!')
            break

