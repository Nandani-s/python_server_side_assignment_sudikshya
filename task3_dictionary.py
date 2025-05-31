students={}

def add_student():
    roll = input("Roll number: ")
    name = input("Name: ")
    marks = input("Marks: ")
    contact = input("Contact: ")
    students[roll] = {
        'name': name,
        'marks': marks,
        'contact': contact
    }
    print("Student added successfully!")
    
def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        print("Student found:")
        print("Name:", students[roll]['name'])
        print("Marks:", students[roll]['marks'])
        print("Contact:", students[roll]['contact'])
    else:
        print("Student not found.")
       
def display_all():
    if not students:
        print("No students found.")
    else:
        print(" \n All students:")
        for roll, info in students.items():
            print(f"Roll: {roll}, Name: {info['name']}, Marks: {info['marks']}, Contact: {info['contact']}")    
            print("----------------------------------------------") 
            
while True:
    print("\nMenu:")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Display All Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        search_student()
    elif choice == '3':
        display_all()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")