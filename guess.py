import random

# Generate a random number between 1 and 100
secret_num = random.randint(1, 100)

# Ask the player to guess the number
guess = int(input("Enter a guess: "))

# Keep asking the player to guess until they get it right
while guess != secret_num:
    if guess < secret_num:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")
    guess = int(input("Enter a guess: "))

print("Congratulations! You guessed the correct number.")
