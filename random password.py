import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return

    # Ensure the password contains at least one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Remaining characters
    all_characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle to make the password random
    random.shuffle(password)

    return "".join(password)


try:
    length = int(input("Enter password length: "))

    if length < 4:
        print("Please enter a length of at least 4.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Invalid input! Please enter a valid number.")