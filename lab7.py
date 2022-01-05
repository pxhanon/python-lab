# Lab 7-1

# text = input("Enter text : ")
#
# new_text = ""
#
# ignore_char = ["/", ".", "-", "?", "!", '"', "'", "(", ")", "{", "}", ",", ";", "   "]
#
# for char in range(len(text)):
#     if text[char] not in ignore_char:
#         new_text += text[char]
#
# print(f"-- {new_text} --")

# Lab 7-2

# symbol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz1234567890,.?!"
# cipher = ",.?!MNOPQRSTUVWXYZABCDEFGHIJKLlmnopqrstuvwxyzabcdefghijk 1234567890"
#
# symbol_list = []
# cipher_list = []
#
# for sub_symbol in symbol:
#     symbol_list += sub_symbol
#
# for sub_cipher in cipher:
#     cipher_list += sub_cipher
#
# text = input("Enter your message : ")
#
# cipher_text = ""
#
# for char in text:
#     index = symbol.index(char)
#     cipher_text += cipher_list[index]
#
# print(f"cipher text : {cipher_text}")


# Lab 7-3

# text = input("Enter some text : ")
#
# number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
#
# count_middle = 0
# count_id = 0
#
# for char in range(len(text)):
#     if text[char] == "6" and text[char + 1] == "2" and text[char + 8] == "2" and text[char + 9] == "3":
#         for middle in range(char + 2, char + 8):
#             if text[middle] in number:
#                 count_middle += 1
#                 if count_middle == 6:
#                     count_id += 1
#             else:
#                 break
#         count_middle = 0
#
# print(f"There are {count_id} student IDs.")

# Lab7-4

# text = input("Enter some text : ")
#
# count_parenthesis = 0
# inner_parenthesis = 0
# inner_parenthesis_true_or_false = False
#
# list_paren = []
#
# for char in range(len(text)):
#     if text[char] == "(":
#         for i in range(char + 1, len(text)):
#             if text[i] == "(":
#                 inner_parenthesis += 1
#                 inner_parenthesis_true_or_false = True
#             elif text[i] == ")":
#                 if inner_parenthesis == 0:
#                     count_parenthesis += 1
#                     break
#                 else:
#                     inner_parenthesis -= 1
#
#     if inner_parenthesis_true_or_false:
#         break
#
# print(f"There are {count_parenthesis} pairs of ().")




