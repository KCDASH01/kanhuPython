# Task 1: Create a Dictionary of Student Marks

# Create a dictionary with student names as keys and marks as values
student_marks = {"Alice": 85, "John": 92, "Sandy": 78, "Sayel": 88, "Gotham": 95
}

# Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Retrieve and display the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")