# s = input()

# count = 0
# current = ""
# val = []

# for letter in s:
#     current = current + letter

#     if letter == "L":
#         count = count + 1
#     else:
#         count = count - 1

#     if count == 0:
#         val.append(current)
#         current = ""

# print(len(val))
# for p in val:
#     print(p)


# numbers = [10, 20, 30]
# print(numbers[0])


# def numbers(*args):
#     total = 0
#     for num in args:
#         total = total + num
#     return total


# print(numbers(10, 20, 30))


import pyautogui
import time


n = int(input("Enter a number: "))

print("You have 5 seconds...")
time.sleep(5)

for i in range(1, n + 1):
    pyautogui.write(" " * (n - i))
    pyautogui.write("*" * i)
    pyautogui.press("enter")
