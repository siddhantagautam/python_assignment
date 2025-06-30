word= input("enter the Words")
a = len(word)
v = ['a', 'e', 'i', 'o', 'u']
for vowel in v:
	word = word.replace(vowel, "")
b = len(word)
print(a - b)
