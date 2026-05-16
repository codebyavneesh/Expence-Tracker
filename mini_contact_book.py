print("============ Mini Contact Book ============\n")

contacts = {}

def add_contact():
    name = input("Enter name: ")
    
    if name in contacts:
        print("Contact already exists !!")
    else:
        number = input("Enter mobile number: ")
        contacts[name] = number
        print("------------ Contact Added Successfully ------------\n")
    
def search_contact():
    name = input("Enter name: ")
    
    if name in contacts:
        print(f"{name} : {contacts[name]}")
    
    else:
        print("Contact not found !!")

def update_student():
    name = input("Enter name: ")
    
    if name in contacts:
        number = input("Enter new mobile number: ")
        contacts[name] = number
        print("--------------Contact Updated Successfully------------------\n")
    
    else:
        print("Contact not found !!")

def delete_contact():
    name = input("Enter name: ")
    
    if name in contacts:
        del contacts[name]
        print("------------ Contact Deleted Successfully ----------\n")
    
    else:
        print("Contact not found !!")

def view_contact():
    if not contacts:
        print("No Contacts available !!")
    
    else:
        print("------------- Contacts List ---------------\n")
        
        for name, numbers in contacts.items():
            print(f"{name} : {numbers}")


while True:
    print("\n------------ Contact Book Menu --------------")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. View All Contact")
    print("6. Exit")
    
    
    try:
        choice = int(input("Enter choice: "))
        
        if choice==1:
            add_contact()
        elif choice==2:
            search_contact()
        elif choice==3:
            update_student()
        elif choice==4:
            delete_contact()
        elif choice==5:
            view_contact()
        elif choice==6:
            print("Thank using contact book !!")
            break
        else:
            print("Invalid choice !! try again.")
    
    except ValueError:
        print("Please enter a valid number !!")