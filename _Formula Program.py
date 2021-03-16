import quadratic, trapezium, circle, sphere

def menu():
    print("1. Quadratic")
    print("2. Trapezium area")
    print("3. Circle area")
    print("4. Circle circumference")
    print("5. Sphere volume")
    print("6. Sphere surface area")
    i = input("\nWhat is the number of the equation you would like to solve? ")
    return i

def findEquation():
    if formula == "1":
        quadratic.solve()
    elif formula == "2":
        trapezium.solve()
    elif formula == "3":
        circle.solveArea()
    elif formula == "4":
        circle.solveCircumference()
    elif formula == "5":
        sphere.solveVolume()
    elif formula == "6":
        sphere.solveSurface()
        
print("---------- Welcome to the Advanced Formulae Program ----------")
print("These are our currently available formulae:\n ")
formula = menu()

# reload
while True:
    findEquation()
    again = input("\nWould you like to enter another equation? (y/n)\n")
    if again == "y":
        print("\nReloading...\n")
    else:
        break
    
    
