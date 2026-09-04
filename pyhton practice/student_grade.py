students ={
    "rohit": "A",
    "rahul": "B",
    "raj": "C"
}

print("current student grades")
for name, grade in students.item():
    print(name, "- " ,grade)
print("\n add student")
print("\n2. update student")
print("\n3.print all grades")
choice = int(input("enter your choice"))
if choice == 1:
    name = input("enter name")
    grade = input("enter grade")
    if name in students:
        print("student alredy exists")
    else:
        students[name] = grade
        print("student added")
elif choice == 2:
    name = input("enter name") 
    if name in students:
        new_grade = input("enter new grade")
        students[name] = new_grade
        print("student updated")
    else:
        print("student not found")
else:
    print("invalid choice")


    