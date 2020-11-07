import math

#accounts for both positive and negative y values by solving for y in the equation of a circle
def CircleEq (x, centerX, centerY, radius, sign):
    return centerY + sign * math.sqrt(radius**2 - (x-centerX)**2)

#simplifies finding length
def lengthBetweenPoints (x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

point1 = input("What is the first point? (in (x,y) form) ")
xA = float(point1[1])
yA = float(point1[3])

point2 = input("What is the second point? (in (x,y) form) ")
xB = float(point2[1])
yB = float(point2[3])

point3 = input("What is the third point? (in (x,y) form) ")
xC = float(point3[1])
yC = float(point3[3])

#the actual times do not matter; just the ratio of the times since this assumes constant speed and no obstacles
time1 = float(input("How much time does it take to get to the first point? (no units) "))
time2 = float(input("How much time does it take to get to the second point? (no units) "))
time3 = float(input("How much time does it take to get to the third point? (no units) "))

#r2to3 is never checked but is unncessary
r1to2 = time2/time1
r1to3 = time3/time1

#due to the iterative nature of the program the specificity and margin is required
increment = float(input("What increment level would you like to parse through? "))

#very small margins work along with very small increments based on the times given
margin = float(input("What margin of error is acceptable? "))

#finds the point on the line between the two
xBetweenAandB = ((r1to2*xA) + xB)/(1 + r1to2)
yBetweenAandB = ((r1to2*yA) + yB)/(1 + r1to2)

#finds the point on the line outside the two
xOutsideAandB = ((r1to2*xA) - xB)/(-1 + r1to2)
yOutsideAandB = ((r1to2*yA) - yB)/(-1 + r1to2)

#uses the two points as the diameter of the intended circle
centerX = (xBetweenAandB + xOutsideAandB)/2
centerY = (yBetweenAandB + yOutsideAandB)/2
radius = lengthBetweenPoints(centerX, xBetweenAandB, centerY, yBetweenAandB)

#sets whether it works in case there are no points that satisfy the given conditions
works = False

#range for loops do not work since this doesn't use integer increments
x = centerX - radius

while (centerX - radius <= x <= centerX + radius):
    #accounts for both positive and negative y values per x value
    yPosValue = CircleEq(x, centerX, centerY, radius, +1)
    yNegValue = CircleEq(x, centerX, centerY, radius, -1)
    PDto3 = lengthBetweenPoints(xC, yC, x, yPosValue)
    NDto3 = lengthBetweenPoints(xC, yC, x, yNegValue)
    PDto1 = lengthBetweenPoints(xA, yA, x, yPosValue)
    NDto1 = lengthBetweenPoints(xA, yA, x, yNegValue)

    if (r1to3-margin <= (PDto3/PDto1) <= r1to3+margin):
        print("The triangulated point is: (", x, ",", yPosValue, ").")
        works = True
    elif (r1to3-margin <= (NDto3/NDto1) <= r1to3+margin):
        print("The triangulated point is: (", x, ",", yNegValue, ").")
        works = True

    x += increment

if (works == False):
    print("These coordinates do not work with the time intervals given. Please try again.")
