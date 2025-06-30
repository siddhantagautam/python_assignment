def palindrome(a):
    if str(a) == str(a)[::-1]:
        return True
 

def main():
    a= int(input("Enter the number to check Palindrome"))
    if palindrome(a):
        print(f"{a}is a palindrom")
    else:
        print(f"false, {a} is not a palindrome number")
main()
