color_list1=input("Enetr colors in color_list1(comma.seperated):").split(",")
color_list2=input("Enter colors in color_list2(comma.seperated):").split(",")
color_list1=[color.strip().lower()for color in color_list1]
color_list2=[color.strip().lower() for color in color_list2]
unique_colors=[color for color in color_list1 if color not in color_list2]
print("color in color_list1 not contained in color_list2:")
for color in unique_colors:
	print(color)
