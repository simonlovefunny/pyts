
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


#函数内调用其他函数 1
def f(w):
    return 10*w

def g(x,y):
    return f(3*x) +y

def h(z):
    return f(g(z,f(z+1)))

print(h(1))

#函数内调用其他函数 2
def oneDiget(n):
    return n%10

def largetOnesDiget(x,y):
    return max(oneDiget(x),oneDiget(y))

print(largetOnesDiget(134,694))
print(largetOnesDiget(132,674))

#单元测试函数
def oneDivision(n):
    return n%10
    
def testOneDivision():
    print("Testing oneDivision()...",end="")
    assert(oneDivision(5) == 5)
    assert(oneDivision(123) ==3)
    assert(oneDivision(100) == 1)
    print("Passed!")

testOneDivision()   #报错，断言失败

#局部变量
def f(x):
    print("In f,x= ",x)
    x+=5
    return x

def g(x):
    return f(x*2)+f(x*3)

print(g(2))

#全局变量,一般情况下避免使用全局变量
g = 100

def f(x):
    return x+g

print(f(5))
print(f(6))
print(g)

#修改全局变量的值

g=100

def f(x):
    #当修改一个全局变量的值时，需要声明它是一个全局变量，否则python会认为它是一个局部变量
    global g
    g += 1
    return x+g

print(f(5))
print(f(6))
print(g)


#默认变量

#可以在定义函数的时候定义一个变量，调用函数时缺省对应的变量可以使用默认值，否则使用传入的变量
def f(x,y=10):
    return x+y

print(f(5))
print(f(5,1))


#None return
def f(x):
    x+42
print(f(4)) #None