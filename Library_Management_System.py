print("==================== Library Management System =======================\n")

books = {
    "Python Basic": "Available",
    "C Programming": "Available",
    "Java": "Available",
    "Java Script": "Available",
}

book_issued = {}

def show_book():
    print("\n----------- All Books ------------")
    for book, status in books.items():
        print(f"{book} : {status}")

def issue_book():
    show_book()
    student = input("\nEnter Student name: ").strip().title()
    book = input("Enter book: ").strip().title()
    
    if book not in books:
        print("Book not found !!")
        return
    if books[book] == "Issued":
        print("Books Already Exists !!")
        return
    if student in book_issued:
        print(f"{student} already has a book issued !!")
        return
    
    books[book] = "Issued"
    book_issued[student] = book
    
    print(f"Book {book} successfully issued to {student} !!")

def return_book():
    student = input("Enter student name: ").strip().title()
    
    if student not in book_issued:
        print("Student not found !!")
        return
    else:
        book = book_issued[student]
        books[book] = "Available"
        del book_issued[student]
        print(f"Book {book} returned successfully !!")


while True:
    print("\n----------- Library Management System -------------")
    print("1. Show Menu")
    print("2. Book Issue")
    print("3. Return Book")
    print("4. Exit")
    
    try:
        choice = int(input("Enter choice: "))
    
        if choice == 1:
            show_book()
        elif choice == 2:
            issue_book()
        elif choice == 3:
            return_book()
        elif choice == 4:
            print("Thanks to use my Library Managemet System !!")
            break
        else:
            print("Invalid choice !! try again.")
    except ValueError:
        print("Error: Please enter the option between(1 to 4)")