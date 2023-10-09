##115
#Write a program to display unique vowels present in the given word
vowels=['a','e','i','o','u']
word=input("Enter the word for search of vowels ")
found=[]
for w in word:
    if w in vowels:
        if w not in found:
            found.append(w)
print(found)
print("no of different vowels in word ",word," is ",len(found))