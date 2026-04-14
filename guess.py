import random

def main ():
    secret_number = random.randint(1, 100)
    while True:
        guess = int(input("Guess a number: "))
