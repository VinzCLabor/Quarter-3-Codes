# Create an empty dictionary named student
student = {}

# Use input() to collect data
name = input("Enter your name: ")
age = input("Enter your age: ")
subject = input("Enter your favorite subject: ")

# Store the data into the dictionary with specific keys
student["name"] = name
student["age"] = age
student["subject"] = subject

# Print the student's information in a clear format
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Favorite Subject: {student['subject']}")
