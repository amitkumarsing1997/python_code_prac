##90
## Program to merge character of 2 strings into a single string by taking characters
s1="rutvi"
s2="chavdas"
# s1=input("Enter first String ")
# s2=input("Enter secong string ")
output=""
i,j=0,0
while(i<len(s1) or j<len(s2)):
    if(i<len(s1)):
        output=output+s1[i]
        i=i+1
    if(j<len(s2)):
        output=output+s2[j]
        j=j+1
print(output)