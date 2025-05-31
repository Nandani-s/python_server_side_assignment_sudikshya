import csv

with open("marks.csv","r") as file:
    reader = csv.DictReader(file)
    
    total_marks = 0
    student_count = 0
    
    for row in reader:
        marks = int(row['marks'])
        total_marks += marks
        student_count += 1
    if student_count > 0:
        average_marks = total_marks / student_count
        print("Average marks:", average_marks)
    else:
        print("No students found to calculate average marks.")