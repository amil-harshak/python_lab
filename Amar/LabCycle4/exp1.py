type = int(input("Customer Type: 1. Senior citizen 2. others : "))
principal = int(input("Enter the principal amount : "))
time_period = int(input("Enter the time period : "))

def calculate(p,r,t):
        interest = (p*r*t)/100
        return interest


if type==1:
        SI = calculate(principal,12,time_period)
elif type==2:
        SI = calculate(principal,10,time_period)
else:
        print("Invalid input")
print(SI)


