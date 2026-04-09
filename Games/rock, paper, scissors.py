# This is a simple rock, paper, scissors with computer

import random

dict = {'r': '🪨', 's': '✂️', 'p': '📄'}
rps = ('r','p','s')    
while True:
    lol = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if lol not in rps:
        print("Invalid choice!")
        continue

    ai_choice = random.choice(rps)

    print(f'You chose: {dict[lol]}')
    print(f'Computer chose {dict[ai_choice]}')  
    if lol == ai_choice:
        print("Tie")
    elif ((lol == 'r' and ai_choice == 's')or(lol == 's' and ai_choice == 'r')or(lol == 'p' and ai_choice == 'r')):
        print("You win")
    else:
        print("Computer wins")

    choice = input("Continue? (y/n): ").lower()
    if(choice == 'n'):
        break