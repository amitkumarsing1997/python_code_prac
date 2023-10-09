#114
##it is very easy and compact way of creating list objects from any iterable objects(
##like,list,tuple,dictionary,range etc) based on some condition

##SYNTAX

#list=[expression for item in list if condition]

s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0 ]
print(m)

##Return  first letter of each words in form of string
words=["Balaiah","Nag","Venkatesh","Chiranjeevi"]
l=[w[0] for w in words]
print(l)

## Print num1 which is not available in num2

num1=[10,20,30,40]
num2=[30,40,50,60]
num3=[i for i in num1 if i not in num2]
print(num3)

##common element present in num1 and num2
num4=[i for i in num1 if i in num2]
print(num4)

## print length of each words in string
words="the quick brown for jumps over the lazy dog".split()
print(words)
l=[[w.upper(),len(w)] for w in words]
print(l)


