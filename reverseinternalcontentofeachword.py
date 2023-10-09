#89

## Program ro reverse order of words

s=input("Enter some word with space ")
l1=s.split()
l2=[]
i=len(l1)-1
while i>=0:
    l2.append(l1[i][::-1])
    i=i-1

print(" ".join(l2))