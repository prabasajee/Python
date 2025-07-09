inputfile= open("input.txt", "r")
for line in inputfile:
    line = line.strip()
    if line[2]== 'P':
        print(line)
inputfile.close()