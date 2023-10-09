
## 
##write a program to print characters at odd and even position for the given string

s=input("Enter some string ")

##Ist way
#odd
print(s[0::2])
#even
print(s[1::2])

##2nd way

i=0
len=len(s)-1
print("character at even position")
while i<len:
 print(s[i],end=',')
 i=i+2
print()

print("character at odd position")
i=1
while i<len:
 print(s[i],end=',')
 i=i+2
