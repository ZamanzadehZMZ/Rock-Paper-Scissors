contancts = {}

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
        
def show_all(book) -> str:
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
        print("There isn't this name in phone book!\n")
    else:
        book.pop(delete_name)
    
def 
    
