#grab ddmmss from txt file then convert and write to output file, print amount of data processed
# degree symbol is chr(176)
def ParseDegreeString(ddmmss):
    d = ddmmss
    degreeloc = d.find(chr(176))
    minuteloc = d.find("'")
    secondloc = d.find(chr(34))
    degrees = float(d[0:degreeloc])
    minutes = float(d[degreeloc+1:minuteloc])
    seconds = float(d[minuteloc+1:secondloc])
    return degrees, minutes, seconds

def DDMMSStoDecimal(degrees, minutes, seconds):
    decimaldegree = degrees + minutes/60 + seconds/3600
    return decimaldegree

angles = open("07.Project Angles Input.txt")
output = open("07.Project Angles Output.txt", "w")
x = angles.readline()
record = 0

while x != "":
    angles.readline().replace("\n","")
    degrees, minutes, seconds = ParseDegreeString(x)
    decimaldegree = DDMMSStoDecimal(degrees, minutes, seconds)
    output.write(str(decimaldegree))
    #finding records processed
    record += 1
print(record, "records processed")