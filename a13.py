def multiplication(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
    
def main():
    num = int(input("enter the number for multiplication : "))
    multiplication(num)

main()