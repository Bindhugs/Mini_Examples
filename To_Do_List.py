#To-Do-List

tasks = []

while True:

    print("1. Insert task \n 2. Delete completed task \n 3. View the remaining task \n 4. Exit")
    choice = input("Enter your choice: \n")
    if(choice=="1"):
        work = input("Enter the task: \n")
        tasks.append(work)
        print("Task is added...")   #adds the task into list

    elif(choice=="2"):
        if len(tasks)==0:
            print("No task is available to delete \n")
        else:
            for i in range(len(tasks)):
                print(i+1,"-",tasks[i])
            num = int(input("Enter completed task: "))
            removed = tasks.pop(num-1)
            print("Removed task: ",removed)  #Removes the selected task 

    elif(choice=="3"):
        if len(tasks)==0:
            print("No task to view")
        else:
            print("Viewing the task")
            for i in range(len(tasks)-1,-1,-1):
                print(tasks[i])  #Displays the tasks

    elif(choice=="4"):
        print("Exiting program...")
        break  #Exits the prgm
    
    else:
        print("Invalid option")

