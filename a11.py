def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")


name = input("Enter your name: ")
age = input("Enter your age (or press Enter to skip): ")

# --- Check if age was provided ---
if age.strip() == "":
    greet(name)  # Uses default age = 25
else:
    greet(name, int(age))  # Uses user-provided age