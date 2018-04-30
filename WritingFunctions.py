
#计算三角形的斜边
def hypetenuse(a,b):
    return ((a**2)+(b**2))**0.5

print(hypetenuse(3,4)) #5.0(not 5)
print("---------")

#与非门逻辑
def xor(b1,b2):
    return ((b1 and (not b2)) or (b2 and (not b1)))

print(xor(True,True))  ##False
print(xor(False,False)) # False
print(xor(True,False)) # True
print(xor(False,True)) #True


#函数内调用其他函数
def f(w):
    return 10*w

def g(x,y):
    return f(3*x) +y

def h(z):
    return f(g(z,f(z+1)))

print(h(1))


#None return
def f(x):
    x+42
print(f(4)) #None