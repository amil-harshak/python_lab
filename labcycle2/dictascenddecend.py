mydic={}
l1=int(input("enter the no of elements in the dictionary"))

for i  in range(l1):
        name=input("enter the name:")
        age=input("enter the age:")
        mydic[name]=age
mykeys=list(mydic.keys())
mykeys.sort()
asce={i:mydic[i] for i in mykeys}      
mykeys.sort(reverse=True)
desc={i:mydic[i] for i in mykeys}
print("ascending:",asce)
print("descedim=n:",desc)

