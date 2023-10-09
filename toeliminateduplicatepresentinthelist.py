#131

#approach-1
l=eval(input("Enter List of values: "))
s=set(l)
print(s)

#approach-2

l=eval(input("Enter List of values: "))
l1=[]
for x in l:
    if x not in l1:
        l1.append(x)
print(l1)