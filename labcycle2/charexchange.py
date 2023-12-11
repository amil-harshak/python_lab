string1=input("Enter the string:")
newstring=string1[len(string1)-1:]+string1[1:len(string1)-1]+string1[0:1]
print(newstring)
