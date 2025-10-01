inputfile = open("06.Project Input File.txt", "r")
                  
outputfile = open("06.Project Output File.txt", "w")

mergefile = open("06.Project Merge File.txt")

y = mergefile.readline()
x = inputfile.readline()

i = -1
o = 0
m = 0

#copying input file to output file
while x != "":
    if x == ("**Insert Merge File Here**\n"):
        #copying merge file into output file
        while y != "":
            outputfile.write(y)
            y = mergefile.readline()
            m += 1
        x = '\n'
    outputfile.write(x)
    x = inputfile.readline()
    i += 1
# finding output record
o = i+m
print(i, "input files recorded")
print(m, "merge files recorded")
print(o, "output files recorded")
inputfile.close()
outputfile.close()
mergefile.close()