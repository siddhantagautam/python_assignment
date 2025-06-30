# Swapping using arithmetic operations (without a third variable)222

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"Before swapping First number = {a}, second number = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping : First number = {a}, second  number = {b}")