# program to display all positkions of substring in a given main string
# durga soft page 82

s=input("enter main string")
subs=input("enter sub string")
pos=-1
n=len(s)
flag=False
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("Found at position",pos)
    flag=True
if flag==False:
    print("substring not found")
    
