def play():
    word = input('Enter chosen word: ')
    guessed_letters = set()
    num_guesses = 10

    print(print_word(word, guessed_letters))

    while num_guesses > 0:
        guess = input('Enter chosen character: ')
        if in_word(word, guess):
            guessed_letters.add(guess)
            print('Correct!')
        else:
            num_guesses -= 1
            print(f'Wrong! {num_guesses} guesses left.')
        print(print_word(word, guessed_letters))
        if all(letter in guessed_letters for letter in word):
            print('You guessed the word! You win!')
            break
    else:
        print('You ran out of guesses. You lose!')

def print_word(word, guessed_letters):
    return ' '.join(char if char in guessed_letters else '_' for char in word)

def in_word(word, guess):
    return guess in word
play()
