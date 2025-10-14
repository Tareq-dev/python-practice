
age = int(input("enter your age: "))

if age>=40:
    print("you are eligible for vote")
elif age <= 18:
    print("You are not adult")
elif age >= 18:
    print("You are adult")
else:
    print("You can not eligible for vote")