menu = {"Pizza": "$10", "Burger": '$8', 'Salad': '$6', 'Soda': '$2', 'Coffee': '$3'}

orders = []

while True:
    print("menu \n leave \n bill ")

    user_input = input("What do you want ? : ").lower()

    if(user_input=="menu"):
        print(menu)
    
    elif(user_input == "bill"):
        print("Enter items you consumed?")
        while True:
            item = input("Item(type 'done' to finish): ")
            if item.lower() == 'done':
                break
            if item in menu:
                orders.append(item)
            else:
                print("Item not in menu")
            total = 0
            for item in orders:
                if item in menu:
                    price = int(menu[item].replace("$"," "))
                    total += price
                    print("Your total bill is $",total)
                else:
                    print(item, "not in menu")
    
    elif(user_input == 'leave'):
        print("Sorry if u have had any inconvienence")
        print("And we are happy you enjoyed our resto")
        print("Please visit us again !!")
        break

    else:
        print("Invalid option! Please choose Menu / Bill / Leave")
        break

    
    
    
