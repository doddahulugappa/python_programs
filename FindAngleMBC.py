import math

AB, BC = int(input()), int(input())
hype = math.hypot(AB, BC)  # to calculate hypotenuse
print(hype, "hype AC")
# for DEGREE symbol
degree = chr(176)
acos = math.acos(BC / hype)
print(round(math.degrees(acos), 2), degree, " math.degrees(acos) BC / Hyp", sep='')
asin = round(math.degrees(math.asin(BC / hype)), 2)  # to calculate required angle

print(asin, degree, " math.degrees(asin) BC / Hyp", sep='')

