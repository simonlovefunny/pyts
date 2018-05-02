import math

#Pthon的内置基本类型

def f():
    print("This is a usr_defined function")
    return 42

print("Some basic types in Python.")
print(type(2)) #int
print(type(2.2)) #float
print(type("2.2")) # str(string)
print(type(2 <2.2)) # bool (boolean)
print(type(math))  # module
print(type(math.tan))   # builtin_function_or_method ("function" in Brython)
print(type(f))   # function (user-defined function)
print(type(type(42))) #type


print("####################################")


print("And some types we will see later in the course....")
print(type(Exception())) # Exception
print(type(range(5))) #range
print(type([1,2,3]))  # list
print(type((1,2,3))) #tuple(array)
print(type({1,2,3})) #set
print(type({1:42})) #dict(dictionary or map)
print(type(2+3j))  # complex  (complex number) (we may not see this type)



print("Some builtin constants:")
print(True)
print(False)
print(None)

print("And some more constants in the math module:")
print(math.pi)
print(math.e)

#类型转换
print("Type conversion functions:")
print(bool(0)) #convert to boolean (True or False)
print(float(42)) # convert to a floating point number
print(int(2.8)) # convert to a integer(int)

print("And some basic math functions:")
print(abs(-5)) #absolute value
print(max(2,3)) # return the max value
print(min(3,4)) # return the min value
print(pow(2,3)) # raise to the given  power (pow(x,y) == x**y)
# 精确到小数点后一位
print(round(2.345,1)) # round with the given number of digits

#自动类型转换

print(3 * 2)

print(3 * "abc")  # 输出为 abcabcabc，字符串在python中被认为是列表，列表乘3就是重复三次


#整型除法

print("The / operator does 'normal' float division：")
print(" 5/3 =",(5/3))

print("The // operator does integer division:")
print("5//3 =",(5//3))
print("2//3 =",(2//3))
print("-1//3 =",(-1//3))
print("-4//3 =",(-4//3))

#取余运算

print("The % operator does normal remainder:")

print("5%3 =",(5%3))
print("6%3 =",(6%3))
print("1%3 =",(1%3))
print("0%3 =",(0%3))
print("-6%3 =",(-6%3))
print("-5%3 =",(-5%3))
print("-1%3 =",(-1%3))

#模运算（取余运算）
print(0.1 + 0.1 == 0.2)        # True, but...
print(0.1 + 0.1 + 0.1 == 0.3)  # False!
print(0.1 + 0.1 + 0.1)         # prints 0.30000000000000004 (uh oh)
print((0.1 + 0.1 + 0.1) - 0.3) # prints 5.55111512313e-17 (tiny, but non-zero!)

# 浮点型运算相等和近似相等

print("The problem...")
d1=0.1+0.1+0.1
d2=0.3

print(d1 == d2) # False (never user == with floats!)

#使用一个足够小的数和两个浮点数之差比较
def almostEquals(d1,d2):
    minnum= 10 ** -10
    return (abs(d2 -d1) < minnum)

d1=0.1+0.1+0.1
d2=0.3
print( d1 == d2)
print(almostEquals(d1,d2))

# 短路逻辑
def yes():
    return True

def no():
    return False

def crash():
    return 1/0

print( no() and crash()) # False
print( crash() and no()) # Crash
print(yes() and crash()) # Crash


print( no() or crash()) # False
print( crash() or no()) # Crash
print(yes() or crash()) # Crash

def isPositive(n):
    result=(n>0)
    print("isPositive(",n,") =", result)
    return result

def isEven(n):
    result=(n%2 ==0)
    print("isEven(",n,")=",result)
    return result

print("Test 1:isPositive(4) and isEven(4)")
print(isPositive(4) and isEven(4)) # Calls both functions
print("Test 2:isPositive(-3) and isEven(-3)")
print(isPositive(-3) and isEven(-3)) # Calls only isPositive(n)

#类型和实例
#一般情况下不允许使用type(),而应该使用instance(x,T)
print(type("abc") == str)
print(isinstance("abc",str))

import numbers

def isNumber(x):
    return isinstance(x,numbers.Number) 
    
print(isNumber(1), isNumber(1.1), isNumber(1+2j), isNumber("wow"))



    