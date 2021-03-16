def reverse(s): 
  string = "" 
  for i in s: 
    string = i + string
  return string

def solve():
    a = ""
    b = ""
    c = ""
    amount = 0
    f = input("What is your equation? ( ax^2 + bx + c )\n")
    f = ''.join(f.split())

    # check for negative

    cneg = False
    bneg = False
    length = len(f) - 1
    while length >= 0:
        if f[length] == "-" and cneg == False:
            cneg = True
        elif f[length] == "-":
            bneg = True
        length = length - 1

    # find a value

    if f[0] == "x":
        a = 1
        amount = amount - 1
    else:
        aval = 0
        while f[aval] != "x":         
            aval = aval + 1
        aval = aval - 1
        amount = amount + aval
        while 0 <= (aval):
            a = a + f[aval]
            aval = aval - 1
        a = reverse(a)
        
    # find b value

    blen = len(f) - 5 - amount
    bval = 0
    while blen > bval:
        if f[5 + bval + amount] == "x":
            break
        b = b + f[5 + bval + amount]
        bval = bval + 1
    amount = amount + (bval - 1)

    # find c value
    
    clen = len(f) - 8 - amount
    val = 0
    while clen > val:
        c = c + f[8 + val + amount]
        val = val + 1
    
    # if needed, change b or c values to negative

    if cneg == True:
        c = int(c) * (-1)
    elif bneg == True:
        b = int(b) * (-1)

    # change values to integers, ready for calculations

    a = int(a)
    b = int(b)
    c = int(c)

    # prepare for calculations

    negativeb = b * -1
    squaredb = b ** 2
    fourac = 4 * a * c
    twoa = a * 2

    # do calculations

    step1 = squaredb - fourac
    step2 = step1 ** (1/2)
    step3a = negativeb + step2
    step3b = negativeb - step2
    answer1 = step3a / twoa
    answer2 = step3b / twoa

    # give answers

    print("The first answer is: x = " + str(answer1))
    print("The second answer is: x = " + str(answer2))
