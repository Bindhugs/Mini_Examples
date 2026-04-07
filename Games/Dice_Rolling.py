#It asks the user how many times they want to roll the dice and plays according to that

import random

print("WELCOME TO DICE ROLLING GAME!")

number = input("How many times you want to roll the dice? ")
if(number.isdigit()):
    number = int(number)

    count = 0

    for i in range(number):

        choice = input("Roll the dice (y/n): ").lower()

        if(choice == 'y'):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f'You rolled a {die1} and a {die2}.')
            count+=1
        elif(choice == 'n'):
            print("Thanks for playing hope you enjoyed it 😉")
            break
        else:
            print("Invalid choice. Try again.")
    print("You have rolled the dice: ",count,"times.")

else:
    print("Enter a valid number")