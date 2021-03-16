def solve():
    # inputs
    a = int(input("What is the length of one parallel side? "))
    b = int(input("What is the length of the other parallel side? "))
    h = int(input("What is the perpendicular height? "))

    # calculate
    step1 = (a + b) / 2
    answer = step1 * h

    # print answers
    print("The area of that trapezium would be " + str(round(answer)) + " units.")
    
