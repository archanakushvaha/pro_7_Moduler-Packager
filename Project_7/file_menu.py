FILE_NAME = "log.txt"


def create_file():
    try:
        with open(FILE_NAME, "x") as file:
            file.write("Log File Created\n")

        print("File created successfully.")

    except FileExistsError:
        print("File already exists.")


def write_file():
    with open(FILE_NAME, "w") as file:
        text = input("Enter text: ")
        file.write(text + "\n")

    print("Data written successfully.")


def append_file():
    with open(FILE_NAME, "a") as file:
        text = input("Enter text to add: ")
        file.write(text + "\n")

    print("Data added successfully.")


def read_file():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.read()

        print("\nFile Content:")
        print(data)

    except FileNotFoundError:
        print("File not found. Create the file first.")


def file_menu():
    while True:
        print("\n--- File Operations ---")
        print("1. Create File")
        print("2. Write File")
        print("3. Append File")
        print("4. Read File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()

        elif choice == "2":
            write_file()

        elif choice == "3":
            append_file()

        elif choice == "4":
            read_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")
