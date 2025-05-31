print("Student list:")

student_file = open("students.txt","w") 
while True:
    name = input("Enter student name:")
    if name.lower()== "exit":
        break
    student_file.write(name + "\n")

student_file.close()
print("\n All the students")

student_file = open("students.txt","r")
for student in student_file:
    print( student.strip())

student_file.close()