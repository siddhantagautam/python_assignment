def piramid(a):
     for i in range(1, a + 1):
       spaces = a - i
       stars = 2 * i - 1
       print(" " * spaces + "*" * stars)

def main():
        a = int(input("Enter number of rows: "))
        piramid(a)
main()