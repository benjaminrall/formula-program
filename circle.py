import math

pi = math.pi
def solveArea():
    #values
    r = int(input("What is the radius of the circle? "))

    #solve
    answer = (r ** 2) * pi

    #print
    print("The area of your circle is " + str(round(answer, 3)))

def solveCircumference():
    #values
    r = int(input("What is the radius of the circle? "))

    #solve
    answer = (2 * r) * pi

    #print
    print("The circumference of your circle is " + str(round(answer, 3)))

