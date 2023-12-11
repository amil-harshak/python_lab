l1=input("enter the values (comma seprated):")
l1=[int(x) for x in l1.split(",")]

p_list=[x for x in l1 if x>0]
print("list of positive ",p_list)

sq_list=[x**2 for x in l1]
print("list of squares",sq_list)

str=input("enter a string:")
v=[x for x in str if x in 'AaEeOoIiUu']
print(v)
o=[ord(x) for x in str]
print("ordinal values of each element in the string :",str,"is",o)
