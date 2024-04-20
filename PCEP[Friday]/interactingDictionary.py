
dictionary = {}

def main_menu():
    print("\n*** Interactive Dictionary ***")
    print("1. Add a Definition")
    print("2. Retrieve a Definition")
    print("3. Update a Definition")
    print("4. Remove a Definition")
    print("5. List All Words")
    print("6. Exit")

def add_definition():
    word = input("Enter the word: ")
    definition = input("Enter the definition: ")
    dictionary[word] = definition
    print("Definition added successfully!")

def retrieve_definition():
    word = input("Enter the word to retrieve its definition: ")
    if word in dictionary:
        print(f"The definition of '{word}' is: {dictionary[word]}")
    else:
        print("Word not found in the dictionary.")

def update_definition():
    word = input("Enter the word whose definition you want to update: ")
    if word in dictionary:
        new_definition = input("Enter the new definition: ")
        dictionary[word] = new_definition
        print("Definition updated successfully!")
    else:
        print("Word not found in the dictionary.")


def remove_definition():
    word = input("Enter the word you want to remove: ")
    if word in dictionary:
        del dictionary[word]
        print("Word removed successfully!")
    else:
        print("Word not found in the dictionary.")

def list_all_words():
    print("List of words in the dictionary:")
    for word in dictionary:
        print(word)


def main():
    while True:
        main_menu()
        choice = input("Ener your choice: ")

        if choice == '1':
            add_definition()
        elif choice == '2':
            retrieve_definition()
        elif choice == '3':
            update_definition()
        elif choice == '4':
            remove_definition()
        elif choice == '5':
            list_all_words()
        elif choice == '6':
            print("Exiting the INteractive Dictionary. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()









