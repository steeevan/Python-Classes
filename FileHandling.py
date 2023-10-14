def new_file():
    name = input("What would you like to name your file?":)

    try:
        with open(name, 'w') as file:
            data = input("You may type what you would like:")
            choice = input("Would you like to exit?(yes or no)":)
            if choice == yes:
                exit new_file
            else:
                pass
            print(data)
            print(choice)
            file.write(data + "/n")

            print("Your information has been saved")

def read_file():
    name = input("Enter the what you are trying to read: ")
    
    try:
        with open(name, 'r') as file:
            content = file.read()
            print("name")
            print(content)
