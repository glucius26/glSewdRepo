name = str(input("Enter Name: "))
subjects = []
grades = []

for i in range(1, 6):
    subjects.append(str(input("Enter Subject: ")))
    grades.append(float(input("Enter Grade: ")))

av = sum(grades) / len(grades)

print("Report Card")
print(f"Student: {name}")
print(" ")
print(f"{subjects[0]} grade is {grades[0]}")
print(f"{subjects[1]} grade is {grades[1]}")
print(f"{subjects[2]} grade is {grades[2]}")
print(f"{subjects[3]} grade is {grades[3]}")
print(f"{subjects[4]} grade is {grades[4]}")
print(" ")
print(f"Average grade: {av}")

if av >= 90:
    print("Letter grade: A")
elif av >= 80:
    print("Letter grade: B")
elif av >= 70:
    print("Letter Grade: C")
elif av >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")