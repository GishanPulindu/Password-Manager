print("---Welcome to My Password Manager---")
print("""Enter a command from following below :
save - To save password
view - To view stored passwords
search - To search an entry
exit - To exit the program
""")


def save_password(w, u, p):
    if not duplicate_detect(website, username):
        with open("PasswordManager.txt", "a", encoding="utf-8") as f1:
            f1.write(f"{w}, {u}, {p}\n")
            print("Information stored successfully!")
        return


def view_password():
    try:
        with open("PasswordManager.txt", "r", encoding="utf-8") as f2:
            content = f2.readlines()
            for i in content:
                print(i.rstrip("\n"))
    except FileNotFoundError:
        print("Nothing to view! Save a password first.")
    return


def search_password(e):
    try:
        with open("PasswordManager.txt", "r", encoding="utf-8") as f3:
            content = f3.readlines()
            for i in content:
                if e.lower() in i.lower():
                    print(i)
                else:
                    print("Not found! Save first.")
    except FileNotFoundError:
        print("Password save file not found! Run save command once.")
    return


def duplicate_detect(w, u):
    try:
        with open("PasswordManager.txt", "r", encoding="utf-8") as f4:
            content = f4.readlines()
            for i in content:
                if (w in i) and (u in i):
                    print("Duplicate Detected")
                    return True
                else:
                    return False
    except FileNotFoundError:
        with open("PasswordManager.txt", "a", encoding="utf-8") as file:
            print("Save File created!")


while True:
    command = input("Enter a command to run: ")
    if command.lower() == "save":
        website = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if website and username and password:
            save_password(website, username, password)
        else:
            print("Enter Values to the given inputs!")
    elif command.lower() == "view":
        view_password()
    elif command.lower() == "search":
        entry = input("Search an entry: ")
        if entry:
            search_password(entry)
        else:
            print("Enter a value for the entry to search!")
    elif command.lower() == "exit":
        break
    else:
        print("Enter a valid command!")
