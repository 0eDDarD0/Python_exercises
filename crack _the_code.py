#Let's build a game where th euser will try to guess a strign of 4 different random numbers
#The user will try to guess the secret number in the least number of attemps by hinting the number of correct guesses and coincidences

import random

def buildCode():
    '''Returns a string of 4 different random numbers'''

    code = str(random.randint(0, 9))

    while len(code) < 4:
        num = str(random.randint(0, 9))
        if num not in code:
            code += num

    return code


def guessAttempt(guess, code):
    '''Receives the user's attempt and the code and returns a dict with the number of "guesses" and "coincidences"'''

    score = {"coincidences": 0, "guesses": 0}

    for i in guess:
        if i in code:
            if guess.index(i) == code.index(i):
                score["guesses"] += 1
            else:
                score["coincidences"] += 1

    return score


end = False;
code = buildCode()
while not end:
    guess = input("Try to guess the 4 digit number: ")
    
    score = guessAttempt(guess, code)  

    if score["guesses"] == 4:
        end = True
    else:
        print("You got " + str(score["guesses"]) + " guesses and " + str(score["coincidences"]) + " coincidences")


print("YOU WON!!!")