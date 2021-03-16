import math
pi = math.pi

def solveVolume():
    #input
    r = int(input("What is the radius of the sphere? "))

    #calculate
    answer = (4/3) * pi * (r ** 3)

    #print
    print("The volume of that sphere would be " + str(round(answer, 3)))

def solveSurface():
    #input
    r = int(input("What is the radius of the sphere? "))

    #calculate
    answer = 4 * pi * (r ** 2)

    #print
    print("The surface area of that sphere would be " + str(round(answer, 3)))
