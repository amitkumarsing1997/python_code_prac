#148
##Variable length arguments
##Sometimes we can pass variable number of arguments to our function,such type of arguments are called
## variable length arguments
##We can declare a variable length argument with * symbol as follows Example= f1(*n)
## We can call this function by passing any number of arguments including zero number 
## Internally all these values represented in the form of tuple

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print("The Sum= ",total)

sum()
sum(10)
sum(10,20,30,40)

#######

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)

f1(10)
f1(10,20,30,40)

### after variable length argument if we are taking any other arguments then we should provide values as keyword argumetns

def f1(*s,n1):
    for s1 in s:
        print(s1)
    print(n1)
    
f1("A","B",n1=10)
## f1("A","B",10) this will throw error because last argument 10 is not keyword arguments


# NOTE= We can declare key word variable length arguments also.
## for this we have to use **

# def f1(**n):
#We can call this function by passing any number of keyword arguments .Internally these keyword
# arguments will be stored inside a dictionary

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Durga",marks=70,subject="Java")


##ANONYMOUS FUNCTION
#Sometime we delclare a function wqithout any name such type of nameless functions are called anonymous function or lambda functions

###The main purpose of anonymous function is just for instant use(or for one time usage)

##Normal Function
#

## lambda function'
#lambda n:n*n

## suyntax

#lambda argument_list:expression


## lambda function to find biggest of given values

s=lambda a,b:a if a>b else b
print("The Biggest of 20,10 is: ",s(20,10))
print("the biggest of 100,200 is ",s(100,200))


## Profgram to filter only even numbers from list by using filter()

def isEven(x):
    if x%2==0:
        return True
    else:
        return False
    
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)

##With lambda function
l=[0,5,10,15,20,25,30]
l1=list(filter(lambda x:x%2==0,l))
print(l1)
l2=list(filter(lambda x:x%2!=0,l))
print(l2)


## reduce() function:
# reduce() function reduces sequence of elements into a single element by applying the specified function
## reduce(function,sequence)
# reduce() functionn present in functools module and hence we should write import statement

from functools import *
l=[10,20,30,40,50]
result=reduce(lambda x,y:x+y,l)
print(result)

##Function Aliasing:
# for the existing functtion we can give another name, which is nothing but function aliasing

def wish(name):
    print("Good morning: ",name)

greeting=wish
print(id(wish))
print(id(greeting))

greeting("Durga")
wish("Durga")

s