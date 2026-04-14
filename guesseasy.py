import random

def main ():
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number: "))

        if guess > secret_number:
            print("Too high!")

        elif guess < secret_number:
            print("Too low!")
            
        else:
            print("Correct!")
            break

main()