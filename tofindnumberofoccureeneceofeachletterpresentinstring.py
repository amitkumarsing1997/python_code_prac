#139
#Write a program to find number of occurrences of each letter present in the given string

word=input("Enter any word ")
d={}
for x in word:
    d[x]=d.get(x,0)+1
    for k,v in d.items():
        print(k," occurred ",v," times")