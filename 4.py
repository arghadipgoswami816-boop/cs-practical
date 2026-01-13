#4. Remove all the line that contain the character "a" in the file and write to another file.
with open('input.txt','r') as src, open('output.txt','w')as dest:
    for line in src:
        if 'a' not in line and 'A' not in line:
            dest.write(line)
