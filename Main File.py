# number1 = 1
# number2 = 3
# number3 =5
# print(number1 + number2 + number3)
#
#
# number1 = 2
# number2 = 4
# number3 =6
# print(number1 * number2 * number3)
#
#
# diagonal1 = 4
# diagonal2 = 8
# print(diagonal1 * diagonal2 / 2)
#
#
# diag1 = 6
# diag2 = 11
# result = diag1 * diag2 / 2
# print(result)
#
#
# digit1 = int(input("Enter first number: "))
# digit2 = int(input("Enter second number: "))
# digit3 = int(input("Enter third number: "))
# digit4 = int(input("Enter forth number: "))
# result = digit1 * digit2 * digit3 * digit4
# print(result)
#
#
# number = int(input("Enter 4-digit number: "))
# # 1246
# num1 = number // 1000
# # v1
# num2 = number % 100 // 20
# # v2
# num3 = number % 100 // 10
# # v3
# num4 = number % 10
# # v4
#
# result = num1 * num2 * num3 * num4
# print(f"num1: {num1} num2: {num2} num3: {num3} num4: {num4}")
# print(f"result: {result}")
#
# print("Hello world", "Nice to meet ya'll", "Welcome", end = " ", sep = ", ")
# print("How are you?", end = " ")
# print("Good, thanks")
#
# number1 = 1
# number2 = 3
# number3 =5
# print(number1 + number2 + number3)
#
#
# number1 = 2
# number2 = 4
# number3 =6
# print(number1 * number2 * number3)
#
#
# diagonal1 = 4
# diagonal2 = 8
# print(diagonal1 * diagonal2 / 2)
#
#
# diag1 = 6
# diag2 = 11
# result = diag1 * diag2 / 2
# print(result)
#
#
# digit1 = int(input("Enter first number: "))
# digit2 = int(input("Enter second number: "))
# digit3 = int(input("Enter third number: "))
# digit4 = int(input("Enter forth number: "))
# result = digit1 * digit2 * digit3 * digit4
# print(result)
#
# papapasokafkasd
#
# number = int(input("Enter 4-digit number: "))
# # 1246
# num1 = number // 1000
# # v1
# num2 = number % 100 // 20
# # v2
# num3 = number % 100 // 10
# # v3
# num4 = number % 10
# # v4
#
# result = num1 * num2 * num3 * num4
# print(f"num1: {num1} num2: {num2} num3: {num3} num4: {num4}")
# print(f"result: {result}")
#
# print("Hello world", "Nice to meet ya'll", "Welcome", end = " ", sep = ", ")
# print("How are you?", end = " ")
# print("Good, thanks")

# hours = int(input("Enter hours: "))
#
# if hours >= 12 and hours <=23:
#     print("PM")
# elif hours >=0 and hours <12:
#     print("AM")
# else:
#     print("Incorrect hours!")

# film_rating = int(input("Enter film rating"))
#
# if film_rating > 0 and film_rating <= 5:
#     if film_rating == 4 or film_rating == 5:
#         print("OK")
#     else:
#         print("NOT OK")
# else: print("INCORRECT RATING")

# HomeWork (12.02.2024)
# print("Hello world")
# ########################
# print("Hello People")

# digit1 = int(input("Enter first number: "))
# digit2 = int(input("Enter second number: "))
# digit3 = int(input("Enter third number: "))
# operation = int(input("1 - Minimum, 2 - Maximum, 3 - Average"))
#
# if operation == 1:
#     if digit1 < digit2 < digit3:
#         print(f"Minimum: {digit1}")
#     elif digit2 < digit3 < digit1:
#         print(f"Minimum: {digit2}")
#     elif digit3 < digit2 < digit1:
#         print(f"Minimum: {digit3}")
# elif operation == 2:
#     if digit1 > digit2 > digit3:
#         print(f"Maximum: {digit1}")
#     elif digit2 > digit3 > digit1:
#         print(f"Maximum: {digit2}")
#     elif digit3 > digit2 >digit1:
#         print(f"Maximum: {digit3}")
# elif operation == 3:
#     print(f"Average: {digit1 +digit2 +digit3 / 3}")
# else:
#     print("Incorrect input")


value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))
value3 = int(input("Enter third number: "))
action = int(input("1 - Miles: , 2 - Inches: , 3 - Yards: "))

if action == 1:
    print(f"Miles: {value1 / 1609}")
elif action == 2:
    print(f"Inches: {value2 * 39}")
elif action == 3:
    print(f"Yards: {value3 * 1.09}")