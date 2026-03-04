
student = {}

name = input("Enter your name: ")
age = input("Enter your age: ")
subject = input("Enter your favorite subject: ")

student["name"] = name
student["age"] = age
student["subject"] = subject

print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
