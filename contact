names = []
phones = []
birthdays = []

def save_contacts():
    with open("contacts.txt", "w") as file:
        for i in range(len(names)):
            file.write(names[i] + "," + phones[i] + "," + birthdays[i] + "\n")
    print("Contacts saved successfully")

def load_contacts():
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                names.append(data[0])
                phones.append(data[1])
                birthdays.append(data[2])
        print("Contacts loaded successfully!")
    except:
        print("No saved contact found.")

load_contacts()

while True:
    print("\n=== My Contact List ===")
    print("1. Add new contact")
    print("2. Display all contacts")
    print("3. Save Contacts")
    print("4. Exit")

    choice = input("What would you like to do? (1/2/3/4): ").strip()

    if choice == "4":
        print("Goodbye!")
        break

    elif choice == "1":
        print("\nAdding new contact...")
        new_name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        birthday = input("Enter Birthday:").strip()

        names.append(new_name)
        phones.append(phone)
        birthdays.append(birthday)
        
        print("Contact added successfully!")

    elif choice == "2":
        if not names:
            print("\nNo contacts yet")
        else:
            print("\nAll Contacts:")
            for i in range(len(names)):
                print(f"\nContact #{i+1}:")
                print(f"Name: {names[i]}")
                print(f"Phone: {phones[i]}")
                print(f"Birthday: {birthdays[i]}")

    elif choice == "3":
        save_contacts()

    else:
        print("Please choose option 1, 2, 3 or 4 only")
