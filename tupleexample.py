##120
t=(40,10,30,20)
## find will not work in list or tuple
#print(t.find(30))
print(t.index(30))

##Tuple packing and Tuple unpacking

# TUPLE PACKING-We can create a tuple by packing a group of variables
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)

# TUPLE UNPACKING-it is the reverse process of tuple packing we can unpack a tuple and assign its value to diffferent variables

t=(10,20,30,40)
a,b,c,d=t
print("a=",a,"b=",b,"c=",c,"d=",d)
