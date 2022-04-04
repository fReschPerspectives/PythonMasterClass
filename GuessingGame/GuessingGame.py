import random

answer = random.randint(1, 10)

guess = None

while guess != answer:
    guess = int(input("Please enter a guess from 1 to 10: "))

    if guess > answer:
        print("Guess lower.")
    elif guess == 0:
        print("You gave up. The answer was {}.".format(answer))
        break
    elif guess < answer:
        print("Guess higher")
    else:
        print("You guessed correctly! The answer was {}.".format(answer))
        break

