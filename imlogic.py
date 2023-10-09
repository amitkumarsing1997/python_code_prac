#90
#Write a program for the following requirement
#i/p a4b3c2
#o/p aaaabbbcc
s=input("Enter some string ")
output=""
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+(int(x)-1)*previous

print(output)
