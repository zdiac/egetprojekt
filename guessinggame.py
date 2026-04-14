import random

def main ():

    difficulty = input("Choose difficulty (easy, medium, hard): ")
    if difficulty == "easy":
        secret_number = random.randint(1, 50)
    elif difficulty == "medium":
        secret_number = random.randint(1, 100)
    elif difficulty == "hard":
        secret_number = random.randint(1, 500)
    else:
        print("Invalid difficulty, defaulting to medium.")
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