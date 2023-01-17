import random

NUM_DIGITS = 3 
MAX_GUESSES = 10


# Return a string made up of NUM_DIGITS unique random digits
def get_secret_number():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''

    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    
    return secret_num


# Returns a string with the pico, fermi, bagels clues for a guess and secret number pair
def get_clues(guess, secret_num):
    if guess == secret_num:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            # A correct digit is in the correct place
            clues.append('Fermi')
        elif guess[i] in secret_num:
            # A correct digit is in the incorrect place
            clues.append('Pico')
    
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all
    else:
        # Sort the clues into alphabetical order so their original order 
        # doesn't give information away
        clues.sort()
        return ' '.join(clues)


# Bagels is a deductive logic game where you must guess a number based on clues
def main():
    print('''Bagels, a deductive logic game.

    I am thinking of a {}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:     That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagels          No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.'''.format(NUM_DIGITS))

    print('I have thought up a number')
    print(f'You have {MAX_GUESSES} guesses to get it')
    
    # This stores the secret number the player needs to guess:
    secret_num = get_secret_number()
    num_guesses = 1

    while num_guesses <= MAX_GUESSES:
        guess = ''
        # Keep looking they enter a valid guess:
        while len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f'Guess #{num_guesses}')
            guess = input('> ')

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break # They're correct, so break out of this loop
            if num_guesses > MAX_GUESSES:
                print('You ran out of guesses')
                print(f'The answer was {secret_num}')

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    
    print('Thanks for playing!')
    

if __name__ == '__main__':
    main()