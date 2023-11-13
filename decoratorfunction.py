#162
#function decorators-
#Decorator is a function which can take a function as argument and extend its functionallity and returns modified 
#function with extended functionality

def decor(func):
    def inner(name):
        if name=="Sunny":
            print("hello Sunny Bad Morning")
        else:
            func(name)
    return inner

@decor
def wish(name):
    print("Hello ",name," Good Morning")

wish("Durga")
wish("Ravi")
wish("Sunny")


#How to call same function with decorator and without decorator

#we should use @decor

def decor(func):
    def inner(name):
        if name=="Sunny":
            print("Hello Sunny Bad Morning ")
        else:
            func(name)
    return inner

def wish(name):
    print("Hello ",name," Good Morning")

decorfunction=decor(wish)
wish("Durga")  #decorator wont be executed
wish("Sunny")  #decorator wont be executed

decorfunction("Durga") #decorator will be executed
decorfunction("Sunny") #decorator will be executed


## second example
def smart_division(func):
    def inner(a,b):
        print("We are dividing",a,"with",b)
        if b==0:
            print("OOPS...cannot divide")
            return
        else:
            return func(a,b)
    return inner

@smart_division
def division(a,b):
    return a/b

print(division(20,2))
print(division(20,0))



##Demo Program for decorator Chaning
def decor(func):
    def inner(name):
        print("First Decor(decor) Function Execution")
        func(name)
    return inner

def decor1(func):
    def inner(name):
        print("second decor(decor1) Execution")
        func(name)
    return inner

@decor1
@decor
def wish(name):
    print("Hello ",name," Good Morning")

wish("Durga")