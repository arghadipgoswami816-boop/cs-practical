#2) read a text file line by line and display each word separated by a hash symbol.

with open("input.txt", "r") as file:
    # Read the file line by line
    for line in file:
        # Remove extra spaces and newline
        words = line.strip().split()
        
        # Join words using '#'
        output = "#".join(words)
        
        # Display the result
        print(output)
