a = int(input('enter the number: '))


def prime(a):
     for i in range(2, a, +1):
        if  a % i == 0:
            return False
         
     return True

if prime(a):
    print(f"{a} is prime")
else:
    print(f"{a} is not prime")