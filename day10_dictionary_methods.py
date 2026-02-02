# Day 10 - Python Restart 2026
# Topic: Dictionary methods

person = {
    "name": "Chitra",
    "age": 26,
    "city": "Dubai"
}

# Keys
print(person.keys())

# Values
print(person.values())

# Items
print(person.items())

# Update dictionary
person.update({"age": 27})
print(person)

# Remove item
person.pop("city")
print(person)

# Clear dictionary
person_copy = person.copy()
person_copy.clear()
print(person_copy)