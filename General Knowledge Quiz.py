# Project 4 - General Knowledge Quiz

print("====================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("====================================")

score = 0

# Question 1
ans = input("1. What is the capital of France? ").strip().lower()
if ans == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Paris\n")

# Question 2
ans = input("2. Which planet is known as the Red Planet? ").strip().lower()
if ans == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Mars\n")

# Question 3
ans = input("3. How many days are there in a leap year? ").strip().lower()
if ans == "366":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: 366\n")

# Question 4
ans = input("4. Which is the largest ocean in the world? ").strip().lower()
if ans == "pacific ocean" or ans == "pacific":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Pacific Ocean\n")

# Question 5
ans = input("5. Which programming language are you learning? ").strip().lower()
if ans == "python":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! Correct answer: Python\n")

print("====================================")
print("Quiz Completed!")
print("Your Score:", score, "/5")

if score == 5:
    print("Excellent! Perfect Score!")
elif score >= 3:
    print("Good Job!")
else:
    print("Keep Practicing!")