inputfile = open("06.Project Input File.txt", "r")
                  
outputfile = open(06.Project Output File.txt", "w")

x = inputfile.read()

if x == "**Insert Merge File Here**":
    mergefile = open("06.Project Merge File.txt")

inputfile.close()
outputfile.close()