# conditional statement and expression

#if statement

def f(x):
    print("A",end="")
    if(x == 0):
        print("B",end="")
        print("C",end="")
    print("D")

f(0)
f(1)

# if else statement
def f(x):
    print("A",end="")
    if(x ==0):
       print("B",end="")
       print("C",end="")
    else:
        print("D",end="")
        if(x == 1):
            print("E",end="")
        else:
            print("F",end="")
    print("G",end="")

f(0)
f(1)
f(2)

# absolute value
def absVal(n):
    if(n >=0 ):
        sign=+1
    else:
        sign=-1
    return sign * n

print("absVal(5) =", absVal(5), "and absVal(-5) =", absVal(-5))

