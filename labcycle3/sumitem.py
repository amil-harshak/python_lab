limit = int(input("Enter the limit : "))
lst = []
sum = 0
print("Enter the elements : ")
for i in range(limit):
        lst.append(input())

for i in range(limit):
        sum = sum + int(lst[i])

print("Sum of the items : ",sum)
