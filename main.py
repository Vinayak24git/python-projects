import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f" what is ur guess b/w 1 and {x} "))
        if guess < random_number:
            print(" too low, guess higher ")
        elif guess > random_number:
            print("too high, guess lower")
            
    print(" yay you've guessed the number correctly")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could be also high , b/c low = high
        feedback = input(f"is {guess} to high (H), too low (L), or correct (C)").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1
    print(" the computer gueesed your number correctly")
computer_guess(10)
guess(10)