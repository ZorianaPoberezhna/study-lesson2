import random


words = ['apple', 'orange', 'wallet', 'door', 'computer', 'food']

def masked_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '*' for letter in word])

def guess_the_word_game():
    word = random.choice(words).lower()
    guessed_letters = set()

    attempts = int(input("Enter number of attempts:"))
    while attempts > 0:
        print(f'Word: {masked_word(word, guessed_letters)}')

        user_input = input("Enter letter or word:").lower()
        if len(user_input) > 1:
            if user_input == word:
                print(f"Congratulations! You guessed the word:{word}")
                break
            else:
                print("Wrong word.")
                attempts -= 1

        elif len(user_input) == 1:
            if user_input in guessed_letters:
                print("You already guessed this letter.")
            elif user_input in word:
                guessed_letters.add(user_input)
                print(f"The letter {user_input} is in the word.")
                if set(word) == guessed_letters:
                    print(f'Congratulations! You guessed the word: {word}')
                    break
            else:
                print(f"The letter isn't in word.")
                attempts -= 1

        else:
            print("Invalid input.")

        print(f"There are still attempts: {attempts}")
    if attempts == 0:
        print(f"You lose. Word: {word}")
#ghbie fewjhb
guess_the_word_game()

