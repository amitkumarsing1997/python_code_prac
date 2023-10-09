#131
## Write a program to print different vowels present in the given word

w=input("Enter word to search for vowels: ")
s=set(w)
v={'a','e','i','o','u'}
d=s.intersection(v)
print(d)