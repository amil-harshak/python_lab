a=int(input("Enter the limit :"))
list=[]
for i in range(0,a):
    n=int(input("Enter the elements:"))
    if n>100 :
        list.append("over")
    else :
        list.append(n)
print(list)
