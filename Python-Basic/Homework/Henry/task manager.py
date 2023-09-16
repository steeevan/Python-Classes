
    
def MainMenu():
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Quit")
    
# empty dictionary
taskList = {}  

    
userInput = 0
while userInput != 4:
    MainMenu()
    userInput = int(input("Enter your choice: "))

    if userInput == 1:
        print("Adding Task")
        title = input("Enter your task title: ")
        description = input("Enter your task description: ")
        taskList[title] = description 
        print("done")
    if userInput == 2:
        print("Ongoing tasks")
        print(taskList)
        MainMenu.wait(1)
        

    if userInput == 3:
        Edit_Task_Input = int(input("Mark as done? Yes = 1, or 2 = No "))
        Edit_Task_Input != 2
        MainMenu()
        print("Canceled")
        Edit_Task_Input == 1
        taskList.clear()  
        print("Task Cleared")
    print("Bye")
    

    

    

