print("\n<====================Expence Tracker===================>")
Expences = []
import datetime

def Add_expence():
    print("\n---------------Add Expence---------------")
    category = input("Enter the Expence Category: ")
    note = input("More Information of Category Expences: ")
    ammount = int(input("Enter the Expence Ammount: "))
    date = input("Enter the Date (YYYY|MM|DD): ")
    
    expence = {
        "category": category,
        "note": note,
        "ammount": ammount,
        "date": date,
    }
    
    Expences.append(expence)
    print("\n----------------Expence Added Successfully-----------------")

def View_expence():
    print("\n------------------View All Expences-------------------")
    count = 1
    for eachExpence in Expences:
        print(f"Number of Expences: {count}--> Category of Expence: {eachExpence['category']}, Note: {eachExpence['note']}, Ammount: {eachExpence['ammount']}, Date: {eachExpence['date']}") 
        count += 1

def Total_ammount():
    print("\n------------------Total Ammount-------------------")
    total = 0
    for eachExpence in Expences:
        total = total + eachExpence["ammount"]
    
    print(f"Total Expence: {total}")
    
while True:
    print("\n<=================Main Menu=================>")
    print("1. Add Expence")
    print("2. View All Expences")
    print("3. Total Expences Ammount")
    print("4. Exit")
    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            Add_expence()

        elif choice == 2:
            View_expence()

        elif choice == 3:
            Total_ammount()

        elif choice == 4:
            print("Exit")
            break
        
        else:
            print("Invalid input by the User !!")
    except ValueError:
        print("Error: Please enter a Valid Number!")