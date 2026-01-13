#2) read a text file line by line and display each word separated by a hash symbol.

# Open the file in read mode.
with open('input.txt', 'r') as file:
    # Read file line by line
    for line in file:
        # Remove multiple and extra spaces
        line = line.strip()
        # split the line into words
        words = line.split()
        # Join words with #
        output = "#".join(words)
        # print the result
        print(output)
