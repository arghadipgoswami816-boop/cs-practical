#3) read a text file and display the number of vowels, consonants 
# and uppercase, lowercase characters in the file.

def count_characters(file_path):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    uppercase_count = 0
    lowercase_count = 0
    vowel_count = 0
    consonant_count = 0

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for char in content:
                if char.isalpha():
                    if char.isupper():
                        uppercase_count += 1
                    elif char.islower():
                        lowercase_count += 1

                    if char in vowels:
                        vowel_count += 1
                    elif char in consonants:
                        consonant_count += 1

        print(f"Uppercase characters: {uppercase_count}")
        print(f"Lowercase characters: {lowercase_count}")
        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'file.txt'
count_characters(file_path) 