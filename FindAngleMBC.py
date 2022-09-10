
import math
AB,BC=int(input()),int(input())
hype=math.hypot(AB,BC)                      #to calculate hypotenuse
print(hype,"hype")
acos = math.acos(BC/hype)
print(math.acos(BC/hype),"math.acos(BC/hype)")
print(math.degrees(acos),"math.degrees(acos)")
res=round(math.degrees(math.asin(BC/hype))) #to calculate required angle
degree=chr(176)                                #for DEGREE symbol
print(res,degree, sep='')

for i in range(256):
    print(chr(i),end=" ")

print(chr(221))