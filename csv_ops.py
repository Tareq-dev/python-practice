import csv

# CSV লেখা
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Tareq", 25])
    writer.writerow(["Rahim", 22])
    writer.writerow(["Rashin", 12])
    writer.writerow(["Mimha", 30])

total_marks = 0
num_students = 0

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader: # হেডার skip করা
        name = row[0]
        marks = int(row[1])
        total_marks += marks
        num_students += 1
        print(f"{name} scored {marks} marks")

average = total_marks / num_students
print(f"\nAverage marks: {average}")