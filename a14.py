def pattrn(a):
    for i in range(1,a+1):
     
        print("*" * i)

def main():
    a = int(input("enter the number of row for your table : "))
    pattrn(a)
   
main()