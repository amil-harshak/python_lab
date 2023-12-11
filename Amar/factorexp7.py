user_input = input("Enter a positive integer: ")

try:
    number = int(user_input)

    if number <= 0:
        print("Please enter a positive integer.")
    else:
        factor = 1
        print(f"The factors of {number} are:")
        while factor <= number:
            if number % factor == 0:
                print(factor)
            factor += 1

except ValueError:
    print("Invalid input. Please enter a valid integer.")
