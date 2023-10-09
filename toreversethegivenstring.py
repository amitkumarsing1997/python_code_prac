#Ist way
print("first way")
s=input("Enter some string ")
print(s[::-1])

#2 nd way
print("second  way")
print("".join(reversed(s)))

#3rd way
print("third way")
i=len(s)-1
target=""
while i>=0:
    target=target+s[i]
    i=i-1
print(target)