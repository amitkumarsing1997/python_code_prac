#140
##Write a program to accept student name and amrks from the keyboard
#and create a dictionary.Also display student marks by taking student name as input

n=int(input("Enter the number of students:"))
d={}
for i in range(n):
    name=input("Enter Student name: ")
    marks=input("Enter Student Marks: ")
    d[name]=marks
while True:
    name=input("Enter Student Name to get Marks: ")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student not found ")
    else:
        print("The Marks of ",name," are ", marks)
    option=input("Do you want to find another student marks[Yes | No]")
    if option=="No":
        break
print("Thanks for using our application")
