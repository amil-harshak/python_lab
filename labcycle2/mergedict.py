dict1={}
dict2={}
l1=int(input("enter no of elements in dictionary 1:"))
l2=int(input("enter no of elements in dictionary 2:"))
for i in range(l1):
        name=input("enter the name:")
        age=input("enter the age:")
        dict1[name]=age
for i in range(l2):
        name=input("enter the name:")
        age=input("enter the age:")
        dict2[name]=age
dict1.update(dict2)
print("merged dictionary is:",dict1)

