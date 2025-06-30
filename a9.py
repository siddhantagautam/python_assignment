def devide(a, b):
 return a/b
    


def main():
    a= int(input("enter the Devidend "))
    b= int(input("enter the devisor"))
    if b == 0 :
       print("Devisor can't br zero")
    else:
       print(devide(a, b))

main()