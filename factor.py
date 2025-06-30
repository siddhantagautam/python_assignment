def factor(n):
    for i in range (1, n+1):
        
        if n%i ==0 :
            print(i, end=' ')

            

n= int(input("Enter a number to find factors : "))
print(f"the factors of {n} is:", end=' ') 
factor(n)
