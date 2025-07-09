inpitFile=open("inputFile.txt", "r")

passFile=open("passFile.txt", "w")
failFile=open("failFile.txt", "w")
for line in inpitFile:
    line = line.strip()
    if line[2] == "c":
        passFile.write(line + "\n")
    else:
        failFile.write(line + "\n")
inpitFile.close()
passFile.close()
failFile.close()