text = input("Enter some text : ")

number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count_middle = 0
count_id = 0

for char in range(len(text)):
    if text[char] == "6" and text[char + 1] == "2" and text[char + 8] == "2" and text[char + 9] == "3":
        for middle in range(char + 2, char + 8):
            if middle in number:
                count_middle += 1
                if count_middle % 6 == 0:
                    count_id += 1
            else:
                break

print(count_middle)
print(count_id)

print(f"There are {count_id} student IDs.")

