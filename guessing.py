import random

jackpot = random.randint(1,100)
guess = int(input("guesss a numer b/w 1 and 100: "))
counter = 1

while guess != jackpot:
  if guess > jackpot:
    print("guess lower")
  else:
    print("guess higher")
  guess = int(input("guesss a numer b/w 1 and 100: "))
  counter += 1
print("correct guess")
print("no of trys are",counter,"in total")
