# Lab 4-1

# enter_position = input("x, y : ")
# position = enter_position.split(", ")
#
# x = int(position[0])
# y = int(position[1])
#
# if x < 10 and x > 0 and y < 20 and y > 0:
#     print(f"({x}, {y}) is in C")
# elif x >= 10 and x < 40 and y >= 20 and y < 40:
#     print(f"({x}, {y}) is in A")
# elif x <= 0 and x > -40 and y <= 0 and y > -20:
#     print(f"({x}, {y}) is in B")
# else:
#     print(f"({x}, {y}) is in D")

# Lab 4-2

# student_id = input("Enter student ID : ")
# int_student_id = int(student_id)
#
# num_digit = len(student_id) == 10
# front_two_digit = int_student_id // pow(10, 8) in range(48, 63)
# third_digit = (int_student_id // pow(10, 7)) % 10 == 3 or (int_student_id // pow(10, 7)) % 10 == 4 or (int_student_id // pow(10, 7)) % 10 == 7
# back_two_digit = int_student_id % 100 in range(21, 41) or int_student_id % 100 in range(51, 54, 2)
#
# print(num_digit)
# print(front_two_digit)
# print(third_digit)
# print(back_two_digit)
#
# if num_digit and front_two_digit and third_digit and back_two_digit:
#     print("Valid ID")
# else:
#     print("Invalid ID")

# Lab 4-3

# import datetime
#
# student_id = input("Enter student ID : ")
# int_student_id = int(student_id)
#
# front_two_digit = int_student_id // pow(10, 8)
# third_digit_master = (int_student_id // pow(10, 7)) % 10 == 7
# third_digit_bachelor = (int_student_id // pow(10, 7)) % 10 == 3 or (int_student_id // pow(10, 7)) % 10 == 4
# back_two_digit = int_student_id % 100
#
# group1 = [21, 23, 25, 28, 30, 31, 32, 33, 35, 36, 37, 38, 39, 53]
# group2 = [22, 24, 26, 27, 29, 34, 40, 51]
#
# back_two_digit_group1 = back_two_digit in group1
# back_two_digit_group2 = back_two_digit in group2
#
# fee = 0
#
# year = (datetime.date.today().year + 543) % 100
#
# if len(student_id) == 10:
#     if front_two_digit in range(48, 50):
#         semester = int(input("Enter semester : "))
#
#         semester1_2 = semester == 1 or semester == 2
#         semester3 = semester == 3
#
#         if semester != 1 or semester != 2 or semester != 3:
#             print("Invalid semester")
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group1:
#             fee = 16000
#         elif third_digit_bachelor and semester3 and back_two_digit_group1:
#             fee = 4000
#         if third_digit_master and semester1_2 and back_two_digit_group1:
#             fee = 22500
#         elif third_digit_master and semester3 and back_two_digit_group1:
#             fee = 6000
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group2:
#             fee = 12000
#         elif third_digit_bachelor and semester3 and back_two_digit_group2:
#             fee = 4000
#
#         if third_digit_master and semester1_2 and back_two_digit_group2:
#             fee = 16500
#         elif third_digit_master and semester3 and back_two_digit_group2:
#             fee = 6000
#     elif front_two_digit in range(50, 56):
#         semester = int(input("Enter semester : "))
#
#         semester1_2 = semester == 1 or semester == 2
#         semester3 = semester == 3
#
#         if semester != 1 or semester != 2 or semester != 3:
#             print("Invalid semester")
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group1:
#             fee = 18000
#         elif third_digit_bachelor and semester3 and back_two_digit_group1:
#             fee = 4500
#
#         if third_digit_master and semester1_2 and back_two_digit_group1:
#             fee = 26000
#         elif third_digit_master and semester3 and back_two_digit_group1:
#             fee = 7000
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group2:
#             fee = 4500
#         elif third_digit_bachelor and semester3 and back_two_digit_group2:
#             fee = 4500
#
#         if third_digit_master and semester1_2 and back_two_digit_group2:
#             fee = 19000
#         elif third_digit_master and semester3 and back_two_digit_group2:
#             fee = 7000
#     elif front_two_digit >= 56 and front_two_digit <= year:
#         semester = int(input("Enter semester : "))
#
#         semester1_2 = semester == 1 or semester == 2
#         semester3 = semester == 3
#
#         if semester != 1 or semester != 2 or semester != 3:
#             print("Invalid semester")
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group1:
#             fee = 21000
#         elif third_digit_bachelor and semester3 and back_two_digit_group1:
#             fee = 5250
#
#         if third_digit_master and semester1_2 and back_two_digit_group1:
#             fee = 31000
#         elif third_digit_master and semester3 and back_two_digit_group1:
#             fee = 7750
#
#         if third_digit_bachelor and semester1_2 and back_two_digit_group2:
#             fee = 17000
#         elif third_digit_bachelor and semester3 and back_two_digit_group2:
#             fee = 5250
#
#         if third_digit_master and semester1_2 and back_two_digit_group2:
#             fee = 23000
#         elif third_digit_master and semester3 and back_two_digit_group2:
#             fee = 7750
#     elif back_two_digit not in group1 or back_two_digit not in group2:
#         print("Invalid ID")
# else:
#     print("Invalid ID")
#
# if fee != 0:
#     print(f"Registration fee : {fee}")