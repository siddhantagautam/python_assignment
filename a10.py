def max(numbers):
    if not numbers:
        return None  # Handle empty list
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Take input from user
num = input("Enter numbers separated by space: ")
numbers = list(map(int, num.split( )))

#  Call the function and print result
print("The maximum value is:", max(numbers))