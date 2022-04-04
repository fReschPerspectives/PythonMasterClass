def fizz_buzz(n: int = 1) -> str:
    """
    :param n: integer input to the function
    :return: string that is "fizz" if divisible by three,
             "buzz" if is divisible by 5, "fizz_buzz" if 
             divisible by both, or the number if neither.
    """

    if n % 3 == 0 and n % 5 == 0:
        return "fizz buzz" 
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return str(n)


instructions = """
To play Fizz Buzz, enter the word "fizz" if the number is divisible by 3.
Enter the word "buzz" if the number is divisible by 5 and enter the word
"fizz buzz" if divisbile by both 3 and 5. If none of these scenarios is 
correct, enter the turn count.
"""

print(instructions)
turn_count = 1

computer_first = str(input("User or Computer first?")).lower()

if computer_first == "computer":
    iteration = turn_count - 1
else:
    iteration = turn_count


while True:
    answer = fizz_buzz(turn_count)    

    if not iteration % 2 == 0:
        guess = str(input("The turn count is {}. Please enter your response: ".format(turn_count)))

        if guess == answer:
            print("Good Job.")
        else:
            print("So sorry. That is not correct.")
            break
    else:
        print("The turn number is {0}. The answer is {1}.".format(turn_count, fizz_buzz(turn_count)))

    turn_count += 1
    iteration +=1
