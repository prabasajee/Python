inputfile= open("inputFile.txt", "r")
for line in inputfile:
    line = line.strip()
    if line[2]== "c":
        print(line)
inputfile.close()