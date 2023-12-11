def isalldigits_even(number):
        return all(int(digit)%2==0 for digit in str(number))
def generate_square_numbers(start,end):
        square_numbers=[]
        current_numbers=int((start **0.5//2)*2)
        while current_numbers**2<=end:
                     candidate=current_numbers **2
                     if len(str(candidate))==4 and isalldigits_even(candidate):
                         square_numbers.append(candidate)
                     current_numbers+=2
        return square_numbers
start_range=int(input("enter starting range: "))
end_range=int(input("enter end range:  "))
result=generate_square_numbers(start_range,end_range)
print(result)
