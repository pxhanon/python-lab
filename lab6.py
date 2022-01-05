# Lab 6-1

# word = input("Next word : ")
# sentence = ""
#
# while word != ".":
#     sentence += word + " "
#     word = input("Next word : ")
#
# print(sentence)

# Lab 6-2

# enter_integer = int(input("Enter an integer : "))
#
# print(f"{enter_integer} is divisible by : ")
#
# for possible_num in range(1, enter_integer + 1):
#     if enter_integer % possible_num == 0:
#         print(possible_num)

# Lab 6-3

# enter_integer = int(input("Enter an integer : "))
#
# no_prime = False
#
# if enter_integer > 1:
#     for possible_num in range(2, enter_integer):
#         if enter_integer % possible_num == 0:
#             no_prime = True
#             break
#
# if enter_integer == 1:
#     print("1 is not a prime.")
# elif no_prime:
#     print(f"{enter_integer} is not a prime.")
# else:
#     print(f"{enter_integer} is a prime.")

#  Lab6-4

# start_temp = 0
#
# for day in range(1, 8):
#     temp = float(input(f"Day {day} : "))
#     if temp > start_temp:
#         start_temp = temp
#     else:
#         print(f"Temperature dropped on day {day}")
#         start_temp = temp

#  Lab 6-5

# import random
#
# answer = random.randint(1, 9) # 1 to 9
#
# your_guess = int(input("Your guess : "))
#
# while your_guess != answer:
#     your_guess = int(input("Your guess : "))
#
# print("Correct.")
