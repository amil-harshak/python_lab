user_input = input("Enter a positive integer: ")

try:
    number = int(user_input)
    if number <= 0:
        print("Please enter a positive integer.")
    else:
        reversed_number = 0
        while number > 0:
            digit = number % 10
            reversed_number = reversed_number * 10 + digit
            number //= 10

        print(f"The reverse of the given number is: {reversed_number}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
