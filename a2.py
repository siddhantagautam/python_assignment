def dec_to_bin(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary ##  ,,Start: binary = "",,6 % 2 = 0 → binary = “0”,,3 % 2 = 1 → binary = “10”,,1 % 2 = 1 → binary = “110”
        n = n // 2
    return binary


num = int(input("Enter a decimal number: "))
print(f"Binary equivalent: {dec_to_bin(num)}")
