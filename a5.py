# Write a Python program to print the first 10 numbers of the Fibonacci series.

def fibonacci_series():
    a = 0
    b = 1
    c = 0

    while c < 10:
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
        c += 1

fibonacci_series()