#88
s=input("Enter the Some String ")
l1=[]
l=s.split()
#print words in list form
print(l)
i=len(l)-1
# print no of words in list
print(i)
while i>=0:
    l1.append(l[i])
    i=i-1

#print reverse word in form of list
print(l1)

#print reverse word without the list form
print(" ".join(l1))
