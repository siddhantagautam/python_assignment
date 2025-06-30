def age(a):
    if a < 18:
        return "Minor"
    elif 18 <= a < 60:
        return "Adult"
    else:
        return "senior citizen"
    
a= int(input("Enter your age: "))
print(age(a))