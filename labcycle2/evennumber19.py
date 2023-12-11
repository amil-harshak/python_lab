input_str=input("Enetr a list of integers seperated by spaces:")
integer_list=[int(x) for x in input_str.split()]
odd_number=[num for num in integer_list if num%2 !=0]
print("List after remians even number:",odd_number)
