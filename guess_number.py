number = 10
guesses_left = 5

print("I'm thinking of a number... You have 5 guesses.")

while guesses_left > 0:
    guess = input("What number am I thinking of? ")

    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break

    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print(f"Too low. You have {guesses_left - 1} guesses left.")
        else:
            print(f"Too high. You have {guesses_left - 1} guesses left.")
    else:
        print(f"Please try again. You have {guesses_left - 1} guesses left.")

    guesses_left -= 1

if guesses_left == 0:
    print(f"Sorry, you've run out of guesses. The number was {number}.")
