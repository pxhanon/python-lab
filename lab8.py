# # append
#
# f = open("test1.txt", "a")
# f.write("Now the file has more content!")
# f.close()
#
# # open and read the file after the appending:
# f = open("demofile2.txt", "r")
# print(f.read())
#
# # write
#
# f = open("test2.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
#
# # open and read the file after the appending:
# f = open("demofile3.txt", "r")
# print(f.read())
#
# # x = create file

# Lab 8-1

# init_pos = input("Initial position : ")
#
# pos_list = init_pos.split(", ")
#
# x = int(pos_list[0])
# y = int(pos_list[1])
#
# invalid_input = False
#
# file = open("move.txt", "r")
#
# char_list = [line.strip("\n") for line in file if line != "\n"]
#
# for char in char_list:
#     if char == "L":
#         x -= 1
#     elif char == "R":
#         x += 1
#     elif char == "D":
#         y -= 1
#     elif char == "U":
#         y += 1
#     else:
#         invalid_input = True
#         break
#
# if invalid_input:
#     print("Invalid command")
# else:
#     print(f"Robot stops at {x}, {y}")

# Lab 8-2

# init_pos = input("Initial position : ")
#
# pos_list = init_pos.split(", ")
#
# x = int(pos_list[0])
# y = int(pos_list[1])
#
# invalid_input = False
#
# file = open("move.txt", "r")
#
# char_list = [line.strip("\n") for line in file if line != "\n"]
#
# for char in char_list:
#     if char == "L":
#         if x > -9:
#             x -= 1
#     elif char == "R":
#         if x < 9:
#             x += 1
#     elif char == "D":
#         if y > -9:
#             y -= 1
#     elif char == "U":
#         if y < 9:
#             y += 1
#     else:
#         invalid_input = True
#         break
#
# if invalid_input:
#     print("Invalid command")
# else:
#     print(f"Robot stops at {x}, {y}")

# Lab 8-3

# file = open("score.txt", "r")
#
# score_list = [int(line.strip("\n")) for line in file if line != "\n"]
#
# total_score = 0
# min_score = 99999
# max_score = 0
#
# for score in score_list:
#     total_score += score
#     if score < min_score:
#         min_score = score
#     if score > max_score:
#         max_score = score
#
# average_score = total_score / len(score_list)
#
# print(f"Average score = {average_score}")
# print(f"Max score = {max_score}")
# print(f"Min score = {min_score}")