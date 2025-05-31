class Student:
    def _init_(self):
        self.name = ""
        self.roll_number = ""
        self.marks = 0
        
    def input_details(self):
        self.name = input("Enter student name:")
        self.roll_number = input("Enter roll number:")
        self.marks = int(input("Enter marks:"))
        
    def display_details(self):
        print("\n---- Student Details ----")
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Marks:", self.marks)
        print("--------------------------")
        
Student1 = Student()
Student1.input_details()
Student1.display_details()