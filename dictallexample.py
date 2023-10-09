#138
#use of items()
d={100:"durga",200:"ravi",300:"shiva"}
for k,v in d.items():
    print(k,"_",v)



## setdefault
# if the key is already available then this function returns the corressponding values
##if the key is not available then the specified key - value will be added as new item to the dictionary

d={100:"durga",200:"ravi",300:"shiva"}
print(d.setdefault(400,"pavan"))
print(d)
print(d.setdefault(100,"sachin"))
print(d)