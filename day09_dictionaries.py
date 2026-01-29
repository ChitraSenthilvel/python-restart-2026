# Day 09 - Python Restart 2026
# Topic: Dictionaries

# Creating a dictionary
student = {
    "name": "Chitra",
    "age": 25,
    "course": "Python"
}

print(student)

# Accessing values
print(student["name"])
print(student.get("age"))

# Updating values
student["age"] = 26
print(student)

# Adding a new key-value pair
student["city"] = "Dubai"
print(student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)