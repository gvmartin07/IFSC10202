#diameter = r2
#circumference = 2 * pi * r
#area = pi * r^2
from math import pi

def diameter(r):
    print(r*2)
def circumference(r):
    print(2*pi*r)
def area(r):
    print(pi*r**2)

strR = "Radius"
strD = "Diameter"
strC = "Circumference"
strA = "Area"

# Open a file for reading
radius = open("06.01 Radius.txt")
r1 = radius.readline()
r2 = radius.readline()
r3 = radius.readline()
r4 = radius.readline()
radius.close()
d = diameter(r1)
c = circumference(r1)
a = area(r1)
print(f'{strR:>15} {strD:>15} {strC:>15} {strA:>15}')
print(f'{d:>15.5f}')