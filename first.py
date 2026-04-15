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


# for i in range(0, 10):
#     pyautogui.write(
#         "Bbu i love you",
#         interval=0.25,
#     )
#     pyautogui.press("enter")


# import cv2

# cam = cv2.VideoCapture(0)

# while True:
#     _, frame = cam.read()
#     cv2.imshow("my cam", frame)
#     cv2.waitKey(1)


with open("message.txt", "r") as file:
    content = file.read()
    print(content)
