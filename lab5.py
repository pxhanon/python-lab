# Lab 5-1

# username = input("Enter username : ")
#
# while username != "Chanon":
#      username = input("Incorrect. Enter again : ")
#
# print(f"Hello, {username}")

# Lab 5-2

# username = input("Enter username : ")
#
# maximum_incorrect = 3
#
# while username != "Chanon" and maximum_incorrect > 1:
#     maximum_incorrect -= 1
#     username = input("Incorrect. Enter again : ")
#
# print(f"Hello, {username}")

# Lab 5-3

# num_of_student = int(input("Number of students : "))
# count = 1
#
# while num_of_student > 0:
#     input(f"Student {count} : ")
#     count += 1
#     num_of_student -= 1

# Lab 5-4

# intermediate_num = float(input("Number of students : "))
# num_of_student = intermediate_num
#
# count = 1
# total_score = 0
# list_score = []
#
# while intermediate_num > 0:
#     score = float(input(f"Student {count} : "))
#
#     total_score += score
#     list_score.append(score)
#
#     count += 1
#     intermediate_num -= 1
#
# average_score = round(total_score / num_of_student, 2)
#
# total_passing_score = 0
# passing_people = 0
# total_failing_score = 0
# failing_people = 0
# highest_score = 0
#
# for score_in_list in list_score:
#     if score_in_list >= 5:
#         total_passing_score += score_in_list
#         passing_people += 1
#
#         if score_in_list > highest_score:
#             highest_score = score_in_list
#     else:
#         total_failing_score += score_in_list
#         failing_people += 1
#
#         if score_in_list > highest_score:
#             highest_score = score_in_list
#
# average_passing_score = total_passing_score / passing_people
# average_failing_score = total_failing_score / failing_people
#
# print(f"Average score : {average_score}")
# print(f"Average passing score : {average_passing_score}")
# print(f"Average failing score : {average_failing_score}")
# print(f"Highest score : {highest_score}")

# Lab 5-5

# balance = 50000
#
# while balance > 0:
#     withdraw = int(input("withdraw : "))
#     balance -= withdraw
#     if balance == 0:
#         print("Balance is 0.")
#     elif withdraw > 50000:
#         print("Insufficient fund.")