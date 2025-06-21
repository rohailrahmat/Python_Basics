# what are scopes in pythons 
# ok scopes means places for variables in python 
#  just like if you place you sweet in secret place no one can access it ,, if you place it in the kitchen anyone can eat it
# just like this python use this kind oof machinism to make scopoes

# python work on LEGB system 
# L = Means local (inside a function)
# E = Means Enclose function (nested Function)
# G = Means Global Funcrtion 
# B = means builtin Funtion (print, loop,etc)



# local function example 

def Func():
    print("this is a local funtion ")
Func()

# nested or Enclose Funtions

def outer():
    hero = "Batman"
    
    def inner():
        print("I love", hero)  # can access 'hero' from the outer function
    
    inner()

outer()


# GLOBAL FUNCTION 
name = "Rohail Rahamt"


def Func3():
    print("Hello", name)

Func3()

# 4. Built-in Scope (B)
print("This is from built-in scope")



# changing global funtion inside a local funtion 
count = 10

def increase():
    global count
    count += 5

increase()
print(count)  # Output: 15





# clousers python 


def multiply_by(n):
    def multiply(x):
        return x * n
    return multiply

times3 = multiply_by(3)
times5 = multiply_by(5)

print(times3(10))  # Output: 30
print(times5(10))  # Output: 50


def outter(num):
    def inner(x):
        return x ** num
    return inner

var_1 = outter(2)
var_2 = outter(3)

print(var_1(3))
print(var_2)


def func1(x):
    def fun2(y):
        return x * y
    return fun2

s = func1(6)

print((8))
