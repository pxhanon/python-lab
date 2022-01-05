# Lab 2-1

# import math
#
# enter_coeff = input("Enter coefficients a, b, c : ")
# coeff = enter_coeff.split(", ")
#
# a = float(coeff[0])
# b = float(coeff[1])
# c = float(coeff[2])
#
# first_answer = (-b + math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
# second_answer = (-b - math.sqrt(pow(b, 2) - 4 * a * c)) / 2 * a
#
# print(f"x = {first_answer}, {second_answer}")

#  Lab 2-2

# enter_coeff = input("Enter coefficients a, b, c : ")
# coeff = enter_coeff.split(", ")
#
# a = float(coeff[0])
# b = float(coeff[1])
# c = float(coeff[2])
#
# critical_point = pow(b, 2) - 4 * a * c
#
# if  critical_point > 0:
#     print("Can use quadratic formula: True")
# else:
#     print("Can use quadratic formula: False")

# Lab 2-3

# enter_today = input("Today date : ")
# today = enter_today.split()
#
# day = int(today[0])
# month = today[1]
# year = int(today[2])
#
# expire_year = year + 4
#
# print(f"Expiration date: {day} {month} {expire_year}")

# Lab 2-4

# enter_lengths = input("Length of 3 sides : ")
# length = enter_lengths.split(", ")
#
# first_side = int(length[0])
# second_side = int(length[1])
# third_side = int(length[2])
#
# if first_side + second_side > third_side and first_side + third_side > second_side and second_side + third_side > first_side:
#     print("Triangle : True")
# else:
#     print("Triangle : False")

# Lab 2-5

# enter_lengths = input("Length of 3 sides : ")
# length = enter_lengths.split(", ")
#
# a = float(length[0])
# b = float(length[1])
# c = float(length[2])
#
# if a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a:
#     print("Right triangle : True")
# else:
#     print("Right triangle : False")


# Lab 2-6

# name = input("Name : ")
#
# if " " in name or "." in name:
#     print(f"{name} contains blank or period : True")
# else:
#     print(f"{name} contains blank or period : False")

