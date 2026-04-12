# numbers = [1, 2, 3, 4, 5]


# for num in numbers:
#     print(num)


# for i in range(1, 6, 3):
#     print(i)


# numbrs = [100, 500, 200]


# largeValue = max(numbrs)
# print(largeValue)


# def double(x):
#     return x * 2


# print(double(5))


# def sum(num1, num2):
#     return num1 + num2


# print(sum(2, 3))


# def fullName(firstName, lastName):
#     name = f"{firstName} {lastName}"
#     print(name)
#     return name


# fullName("John", "Doe")


# def multiply(num1, num2):

#     sum = num1 * num2
#     multiply = sum * 2
#     return multiply, sum


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


players = [
    "Alice",
    "Bob",
    "Charlie",
]

ages = [
    25,
    30,
    22,
]


age_com = []


for player in players:
    for age in ages:
        age_com.append([player, age])


print(age_com)
