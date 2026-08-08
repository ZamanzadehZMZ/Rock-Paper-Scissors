"""
    A simple in-memory phonebook using a dictionary to add, search, show, and delete contacts
"""


contacts = {}

def add_contact(book) -> str :
    name = input('Enter name:\n').lower().strip()
    phone = input('Enter phone:\n').strip()
    
    if name in book:
        answer = input("This contact already exists. Update it? (y/n) : \n").strip().lower()
        if answer == 'y':
            book[name] =phone
            print('Contact changed!\n')
        else:
            print('Contact not changed !\n')
    else:
        book[name]= phone
        print("Contact saved.\n")    
        
def show_all(book) :
    if not book:
        print('Your phone book is empty!\n')
    else:
        for name,phone in book.items():
            print(f'{name} : {phone}')

def search_contact(book):
    name = input("Enter name to search: ").strip().lower()

    if name in book:
        print(f"{name}: {book[name]}\n")
    else:
        print("Contact not found.\n")

def delete_contact(book) -> str:
    delete_name = input('Enter your target name for delete:\n').lower().strip()
    if delete_name not in book:
        print("There isn't this name in the phone book!\n")
        print(f"Contact '{delete_name}' deleted successfully.\n")
        
    else:
        book.pop(delete_name)
    
    
while True:
    print("1. Add contact.")
    print("2. Show all contacts")
    print("3. Search contact")
    print("4. Delete contact ")
    print("5 . Exit")

    option = input('Choise an option:\n')
    
    if option == '1':
        add_contact(contacts)
        
    elif option == '2':
        show_all(contacts)

    elif option == '3':
        search_contact(contacts)

    elif option == '4':
        delete_contact(contacts)

    elif option == '5':
        print("Goodbye!")
        break

    else:
        print("Invalid input!\n")

    