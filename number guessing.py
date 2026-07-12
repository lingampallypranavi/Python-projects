import random

print("===== Number Guessing Game =====")

secret = random.randint(1, 100)

attempts = 0
max_attempts = 7

while attempts < max_attempts:

    guess = int(input("Guess a number (1-100): "))

    attempts += 1

    if guess == secret:
        print("\nCongratulations!")
        print("You guessed the correct number.")
        print("Attempts:", attempts)
        break

    elif guess < secret:
        print("Too Low!")

    else:
        print("Too High!")

    print("Attempts Left:", max_attempts - attempts)

else:
    print("\nGame Over!")
    print("Correct Number was:", secret)