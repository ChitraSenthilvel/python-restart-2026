# Day 13 - Python Restart 2026
# Topic: while loop, break, continue

count = 1

# Basic while loop
while count <= 5:
    print("Count:", count)
    count += 1

print("Loop finished")

# Using break
number = 1
while True:
    if number == 4:
        print("Breaking the loop at", number)
        break
    print(number)
    number += 1

# Using continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Current value:", i)