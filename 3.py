#3.Read a text file and display the number of vowel s and / consonants, /uppercase, / lowercase, character in the file.
vowels = set("aeiouAEIOU")
alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

vc = cc = uc = lc = ch = 0

with open('input.txt', 'r') as f:
    for line in f:
        for c in line:
            ch += 1
            if c in vowels:
                vc += 1
            elif c in alphabet:
                cc += 1

            if c.isupper():
                uc += 1
            elif c.islower():
                lc += 1

print(
    f"Characters: {ch}\n"
    f"Vowels: {vc}\n"
    f"Consonants: {cc}\n"
    f"Uppercase: {uc}\n"
    f"Lowercase: {lc}"
)
