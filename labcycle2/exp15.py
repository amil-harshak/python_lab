input_string = input("Enter the string : ")
first_character = input_string[0]
modified_substring = input_string[1:].replace(first_character, '$')
output_string = first_character + modified_substring
print(output_string)


