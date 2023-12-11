limit = int(input("Enter the limit : "))
first = 0
second = 1
if limit <=0:
        print("Invalid")
elif limit==1:
        print(first)
else:
        print(first)
        print(second)
        for i in range(2,limit):
                temp = first
                first = second
                second = temp+second
                print(second)

