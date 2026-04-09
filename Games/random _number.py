import random
# Number Guessing Game (1–50)
# The program generates a random number and asks the user to guess it.

rand = random.randint(1,100)

while True:
    try:
        number = int(input("Guess the number between 1 to 100: "))
        if (number < rand):
            print("Too low")
        elif (number > rand):
            print("Too high")
        else:
            print("Congragulations! You guessed the number 😉")
    except ValueError:
        print("Please enter a valid number")
    
    
    # Replay option
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
