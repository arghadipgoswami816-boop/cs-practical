#4) To remove all lines that contains a character a in a file and write the rest in a different file.

with open("input.txt", "r") as infile:
    with open("output.txt", "w") as outfile:
        for line in infile:
            # convert line to lowercase before checking
            if 'a' not in line.lower():
                outfile.write(line)

print("Lines containing 'a' or 'A' have been removed and rest is written in output.txt")

