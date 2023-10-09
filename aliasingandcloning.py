#109
##Aliasing and Cloning of List Objects
x=[10,20,30,40]
y=x
print(id(x))
print(id(y))

# the problem in this approach is by using one reference variable if we are changing content,then those 
#changes will be reflected to the other reference varaiable

x=[10,20,30,40]
y=x
y[1]=777
print(x)
print(y)

## To overcome this problem we should go for cloning
##The process of creating exactly duplicate independent objec is called cloning
## we implement cloning by using slice operator or by using copy() function

###Ist By using slice operator
print("cloning by using slice operator")
x=[10,20,30,40]
y=x[:]
y[1]=777
print(x)
print(y)

## 2nd way by using copy functuioon
print("cloning by using copy function ")

x=[10,20,30,40]
y=x.copy()
y[1]=777
print(x)
print(y)