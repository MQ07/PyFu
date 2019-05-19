""" Function without argument """

def printHello():
    print("Hello")

printHello()


""" Function with argument """

def printHi(name):
    print("Hi, " + name)

printHi("Mohammed")


""" Passing default parameters """

def printHi(name = "Mohammed"):
    print("Hi, " + name)

printHi()


""" Passing arguments """

def Sum(a,b,c):
    print(a+b+c)

Sum(10,20,30)

""" Using return statement, store in a variable and print"""

def returnSum(a,b,c):
    return(a+b+c)

x = returnSum(50,60,70)

print(x)


