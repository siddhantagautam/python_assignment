def arrey(numbers):
    if not numbers:
        return None
    a = len(numbers)
    for i in range(0, a):
            if numbers.count(numbers[i]) > 1:
                 return True
            else: return False
           
def main():
     num = input("Enter numbers separated by space: ")
     numbers = list(map(int, num.split( )))
     print(arrey(numbers))

main()