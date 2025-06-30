def add(a , b):
    return a + b


def subtract(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    if b ==0:
        return "Cannot divide by zero"
    else:
        return a / b

def main():
    a = int(input('Enter the first elements:'))
    
    b= (int(input('enter the elements: ')))
    what = int(input('press 1 for addition \n press 2 for subtraction \n press 3 for multiplication \n press 4 for devision\n'))

    if what == 1:
        print(add(a , b)) ##calls the add function

    elif what == 2:
        print(subtract(a , b)) ## calls the subtract function

    elif what == 3:
        print(multiply(a , b)) ## calls the multiply function

    elif what == 4:
        print(divide(a , b)) ## calls the divide function
    
    else:
        print("Invalid choice")

main()