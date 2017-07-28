import random

welcome = "Welcome Code Breaker! Let's see if you can guess my 3 digit number!\n" \
            + "Code has been generated, think of a 3 digit number. \n"
CLOSE = "Close: You've guessed a correct number but in the wrong position"
MATCH = "Match: You've guessed a correct number in the correct position"
NOPE = "Nope: You haven't guess any of the numbers correctly"
WON = "You have broken the code!"

# 3 str objects of none repeating int list
random_number = random.sample('0123456789',3)
print(welcome)

#  True if at least one element in common
def common(guess_number, random_number):
    # convert to sets
    guess_set = set(guess_number)
    number_set = set(random_number)
    common = bool(guess_set & number_set)

    return bool(guess_set & number_set)

# True: correct number in correct position
def match(guess_number, random_number):
    for i in range(len(guess_number)):
        if guess_number[i] == random_number[i]:
            return True
    else:
        return False

# True: correct number, incorrect position
def close(guess_number, random_number):
    if (common(guess_number, random_number)) and (match(guess_number, random_number) != True):
        return True
    else:
        return False

# True: Incorrect numbers
def nope(guess_number, random_number):
    if common(guess_number, random_number) == False:
        return True
    else:
        return False

GAME = True
while GAME:
    guess = input("What is your guess? ")
    guess_str = str(guess)
    guess_number = [i for i in guess_str]

    # test
    # print ("random number =>  ", random_number)
    # print("match =>  ", match(guess_number, random_number))
    # print("close =>  ", close(guess_number, random_number))
    # print("nope =>  ", nope(guess_number, random_number))

    if match(guess_number, random_number):
        print(MATCH)
    if close(guess_number, random_number):
        print(CLOSE)
    if nope(guess_number, random_number):
        print(NOPE)
    if guess_number == random_number:
        print(WON)
        GAME = False
