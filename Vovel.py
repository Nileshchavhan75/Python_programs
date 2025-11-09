# Program to check if an alphabet is a vowel or consonant

vowel = input("Enter an alphabet: ").lower()  # Convert input to lowercase

if vowel in "aeiou":
    print(vowel, "is a Vowel")
else:
    print(vowel, "is Not a Vowel")
