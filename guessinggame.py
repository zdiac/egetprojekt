import random

def main():
    while True:
        difficulty = input("Choose difficulty (easy, medium, hard or quit): ")

        if difficulty == "easy":
            secret_number = random.randint(1, 50)
            break
        elif difficulty == "medium":
            secret_number = random.randint(1, 100)
            break
        elif difficulty == "hard":
            secret_number = random.randint(1, 500)
            break
        elif difficulty == "quit":
            return
        else:
            print("Invalid choice, try again")

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
