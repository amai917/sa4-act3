number = 10

print("I'm thinking of a number...")

while True:
    guess = input("What number am I thinking of? ('q' to quit) ")

    if guess == 'q':
        print(f"Sorry! The number was {number}.")
        break

    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print("Congratulations! You guessed the right number.")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")
