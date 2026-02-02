# Day 12 - Python Restart 2026
# Topic: Comparison & Logical operators

age = 25
has_id = True

# Comparison operators
print(age > 18)
print(age == 25)
print(age != 30)

# Logical operators
if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

is_weekend = False

if not is_weekend:
    print("It's a working day")