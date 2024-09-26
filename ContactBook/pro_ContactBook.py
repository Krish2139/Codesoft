contacts = {}

while True:
    print("Contact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter your name: ")
        if name in contacts:
            print("Contact name {} already exists".format(name))
        else:
            address = input("Enter address: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {'age':address, 'email':email, 'mobile':mobile}
            print("Contact name {} has been created successfully!".format(name))

    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print("Name: {}, Address: {}, Mobile Number: {}, Email: {}".format(name, address, mobile, email))
        else:
            print("Contact not found!")

    elif choice == '3':
        name = input("Enter name to update contact: ")
        if name in contacts:
            address = input("Enter address: ")
            email = input("Enter email: ")
            mobile = input("Enter mobile number: ")
            contacts[name] = {'age':address, 'email':email, 'mobile':mobile}
        else:
            print("Contact not found!")
    
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Contact name {} has been deleted successfully!".format(name))
        else:
            print("Contact not found!")

    elif choice == '5':
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name:
                print("Found Name: {}, Address: {}, Mobile Number: {}, Email: {}".format(name, address, mobile, email))
                found = True
            if not found:
                print("No contact found with that name!")
        
    elif choice == '6':
        print("Total contacts in your book: {}".format(len(contacts)))
    
    elif choice == '7':
        print("Closing the program...")
        break

    else:
        print("Invalid Input!")