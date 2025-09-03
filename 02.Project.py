# distance formula: d = r * arccos(sinx1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2)
from math import pi
from math import acos
from math import sin
from math import cos
# Earth radius = 6371 km
r = int(input("Enter radius of sphere: "))
y1 = int(input("Enter starting point latitude: "))
#converting splat to radians
y1 = int(y1*pi/180)
x1 = int(input("Enter starting point longitude: "))
#converting splog to radians
x1 = int(x1*pi/180)
y2 = int(input("Enter ending point latitude: "))
#converting eplat to radians
y2 = int(y2*pi/180)
x2 = int(input("Enter ending point longitude: "))
#converting eplog to radians
x2 = int(x2*pi/180)
gcdistance = r * acos(sin(x1)) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2)
print(gcdistance)