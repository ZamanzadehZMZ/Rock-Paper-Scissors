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
        
