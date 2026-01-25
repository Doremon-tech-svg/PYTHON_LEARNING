import random

print("🎯 Welcome to the Math Quiz Game!")
print("You will get 5 random addition questions.\n")

score = 0
total_questions = 5

for i in range(1, total_questions + 1):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    correct_answer = num1 + num2

    user_answer = int(input(f"Question {i}: {num1} + {num2} = "))

    if user_answer == correct_answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {correct_answer}\n")

print("📊 Quiz Finished!")
print("Your score:", score, "/", total_questions)

percentage = (score / total_questions) * 100
print("Your percentage:", percentage, "%")

if percentage == 100:
    print("🏆 Perfect score! Amazing job!")
elif percentage >= 60:
    print("👍 Good job! Keep practicing!")
else:
    print("💪 Don't worry, you'll get better with practice!")
