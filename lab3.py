# Lab 3-1

# import math
#
# enter_coeff = input("Enter coefficients a, b, c : ")
# coeff = enter_coeff.split(", ")
#
# a = float(coeff[0])
# b = float(coeff[1])
# c = float(coeff[2])
#
# critical_value = pow(b, 2) - 4 * a * c
#
# if critical_value > 0:
#     first_answer = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
#     second_answer = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
#     print(f"x = {first_answer}, {second_answer}")
# else:
#     print("No real solution.")

# Lab 3-2

# import math
#
# shape = input("Choose circle, square or rectangle : ")
#
# if shape == "circle":
#     radius = float(input("Length of the radius of the circle : "))
#     area_circle = math.pi * pow(radius, 2)
#     print(f"Area is {area_circle}")
# elif shape == "square":
#     side_square = float(input("Length of the side of the square : "))
#     area_square = pow(side_square, 2)
#     print(f"Area is {area_square}")
# elif shape == "rectangle":
#     enter_side_rectangle = input("Length of the side of the rectangle : ")
#     side_rectangle = enter_side_rectangle.split(", ")
#
#     first_side = float(side_rectangle[0])
#     second_side = float(side_rectangle[1])
#
#     area_rectangle = first_side * second_side
#     print(f"Area is {area_rectangle}")
# else:
#     print("Invalid choice.")

# Lab 3-3 type 1

# weight = float(input("Weight (kg.) :"))
# height = float(input("Height (m.) :"))
#
# bmi = weight / pow(height, 2)
#
# if bmi < 18.5:
#     print("ผอม")
# elif bmi >= 18.5 and bmi < 23.0:
#     print("รูปร่างปกติ")
# elif bmi >= 23.0 and bmi < 25.0:
#     print("รูปร่างอ้วน")
# elif bmi >= 25.0 and bmi < 30.0:
#     print("อ้วนระดับ 1")
# else:
#     print("อ้วนระดับ 2")

# Lab 3-3 type 2

# weight = float(input("Weight (kg.) :"))
# height = float(input("Height (m.) :"))
#
# bmi = weight / pow(height, 2)
#
# if bmi >= 30.0:
#     print("อ้วนระดับ 2")
# elif bmi >= 25.0:
#     print("อ้วนระดับ 1")
# elif bmi >= 23.0:
#     print("รูปร่างอ้วน")
# elif bmi >= 18.5:
#     print("รูปร่างปกติ")
# else:
#     print("ผอม")

# Lab 3-4

# enter_weight = input("Weight : ")
# enter_height = input("Height : ")
#
# weight = enter_weight.split()
# if weight[1] == "lbs":
#     si_weight = round(float(weight[0]) * 0.45359237, 1)
# else:
#     si_weight = float(weight[0])
#
# height = enter_height.split()
# if weight[1] == "cm":
#     si_height = round(float(height[0]) * 0.01, 1)
# elif weight[1] == "ft":
#     si_height = round(float(height[0]) * 0.3048, 1)
# else:
#     si_height = float(height[0])
#
# bmi = si_weight / pow(si_height, 2)
#
# if bmi >= 30.0:
#     print("อ้วนระดับ 2")
# elif bmi >= 25.0:
#     print("อ้วนระดับ 1")
# elif bmi >= 23.0:
#     print("รูปร่างอ้วน")
# elif bmi >= 18.5:
#     print("รูปร่างปกติ")
# else:
#     print("ผอม")