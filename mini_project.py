def addtonote():
    with open("mini_project.txt", "a") as f:
        text = input("Write what you want to add to the file:\n")
        f.write("\n" + text)

def viewnote():
    with open("mini_project.txt", "r") as f:
        print(f.read())

def count_words():
    with open("mini_project.txt", "r") as f:
        data = f.read()
        words = data.split()
        print("Total number of words:", len(words))

while True:
    print("\nSimple Notes App")
    print("What do you want to do:")
    print("1. Add a new note")
    print("2. View all notes")
    print("3. Show total number of words")
    print("4. Exit")

    choice = int(input("Enter option (1-4): "))

    if choice == 1:
        addtonote()
        print("Note added!")
    elif choice == 2:
        viewnote()
    elif choice == 3:
        count_words()
    elif choice == 4:
        break
    else:
        print("Invalid option!")