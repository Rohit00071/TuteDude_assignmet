students = {
    "Rohit": "A",
    "Rahul": "B",
    "Sneha": "A"
}

print("Current Student Grades:")
for name, grade in students.items():
    print(name, ":", grade)

print("\n1. Add Student")
print("2. Update Student")
print("3. Print All Grades")

choice = int(input("Enter your choice: "))

if choice == 1:
    name = input("Enter student name: ")
    grade = input("Enter grade: ")

    if name in students:
        print("Student already exists.")
    else:
        students[name] = grade
        print("Student added successfully.")
elif choice == 2:
    name = input("Enter student name: ")

    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print("Grade updated successfully.")
    else:
        print("Student not found.")

elif choice == 3:
    print("\nAll Student Grades:")
    for name, grade in students.items():
        print(name, ":", grade)

else:
    print("Invalid choice.")