# things = "apple", "banana", "cherry"


# if "banansa" in things:
#     print("Yes, 'banana' is in the fruits list")
# else:
#     print("No, 'banana' is not in the fruits list")


# numbers = [10, 56, 41, 11, 11, 45, 45, 78, 98, 100]

# unique_numbers = list(set(numbers))
# print(unique_numbers)


# person = {"name": "John", "age": 30, "city": "New York"}


# for key, val in person.items():
#     print(key, val)


# numbers = [10, 56, 41, 11, 11, 45, 45, 78, 98, 100]


# for i, num in enumerate(numbers):
#     print(i, num)


# from math import *
# from random import *

# result = ceil(3.7)
# # print(result)


# print(randint(1, 10))


# import pyautogui
# from time import sleep

# sleep(5)


# for i in range(0, 100):
#     pyautogui.write(
#         "Tumi akta Kola",
#         interval=0.25,
#     )
#     pyautogui.press("enter")


# import cv2

# cam = cv2.VideoCapture(0)


# print(multiply(2, 3))


# numbers = [1, 2, 3, 4, 5]

# for num in numbers:

#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# height = max(1.75, 1.80, 1.65)
# print(height)


# count = [45, 80, 90, 100]

# count.append(120)
# print(count)


# numbers = [10, 54, 11, 89, 56, 36, 33, 50]


# for num in numbers:
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")


# players = [
#     "Alice",
#     "Bob",
#     "Charlie",
# ]

# ages = [
#     25,
#     30,
#     22,
# ]


# age_com = []


# for player in players:
#     for age in ages:
#         age_com.append([player, age])


# print(age_com)


# things = ["apple", "banana", "cherry"]
# for thing in "apples":
#     print("yes")


# print("hello")


# double = lambda num: num * 2


# print(double(5))


# actors = [
#     {"name": "tom cruise", "age": 56},
#     {"name": "brad pitt", "age": 40},
#     {"name": "tom hanks", "age": 35},
#     {"name": "tom brady", "age": 56},
# ]

# junior = filter(lambda actor: actor["age"] < 50, actors)
# print(list(junior))


n = int(input())
digits = input().strip()

total = sum(int(d) for d in digits)
print(total)
