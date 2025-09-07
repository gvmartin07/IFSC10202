# distance formula: d = r * arccos(sinx1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2)
from math import pi
from math import acos
from math import sin
from math import cos
# Earth radius = 6371 km
r = float(input("Enter radius of sphere: "))
y1 = float(input("Enter starting point latitude: "))
#converting starting point lat to radians
y1 = float(y1*pi/180)
x1 = float(input("Enter starting point longitude: "))
#converting starting point log to radians
x1 = float(x1*pi/180)
y2 = float(input("Enter ending point latitude: "))
#converting ending point lat to radians
y2 = float(y2*pi/180)
x2 = float(input("Enter ending point longitude: "))
#converting ending point log to radians
x2 = float(x2*pi/180)
gcdistance = r * acos(sin(x1)) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2)
print(gcdistance)