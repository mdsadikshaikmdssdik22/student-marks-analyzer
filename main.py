print("===== Student Marks Analyzer =====")

marks = []

n = int(input("Enter number of subjects: "))

# For loop
for i in range(n):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

# While loop
total = 0
i = 0

while i < len(marks):
    total += marks[i]
    i += 1

average = total / n

print("\n===== Result =====")
print("Marks:", marks)
print("Total:", total)
print("Average:", round(average, 2))
print("Highest:", max(marks))
print("Lowest:", min(marks))

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

print("\n===== Subject Marks =====")

for i, mark in enumerate(marks, start=1):
    print(f"Subject {i}: {mark}")
