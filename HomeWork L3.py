# # HomeWork3
#
# try:
#     user_select = int(input("Enter a number to indicate the day of the week: "))
#
#     if user_select == 1:
#         print("Sunday")
#     elif user_select == 2:
#         print("Monday")
#     elif user_select == 3:
#         print("Tuesday")
#     elif user_select == 4:
#         print("Wednesday")
#     elif user_select == 5:
#         print("Thursday")
#     elif user_select == 6:
#         print("Friday")
#     elif user_select == 7:
#         print("Saturday")
#     else:
#         print("Wrong input")
#
#     match user_select:
#         case 1:
#             print("Sunday")
#         case 2:
#             print("Monday")
#         case 3:
#             print("Tuesday")
#         case 4:
#             print("Wednesday")
#         case 5:
#             print("Thursday")
#         case 6:
#             print("Friday")
#         case 7:
#             print("Saturday")
#
# except ValueError as error:
#     print("Please, enter an integer!")
#     print(f"ValueError occurred: {error}")
# except Exception as Error:
#     print(f"Error {Error}")


# try:
#     digit1 = int(input("Enter the first number: "))
#     digit2 = int(input("Enter the second number: "))
#     if digit1 == digit2:
#         digit1, digit2 = digit2, digit1
#         print("Equal numbers")
#     elif digit1 < digit2:
#         print(f"{digit1, digit2}")
#     elif digit1 > digit2:
#         print(f"{digit2, digit1}")
#
# except ValueError as error:
#     print("Please, enter an integer!")
#     print(f"ValueError occurred: {error}")
# except Exception as Error:
#     print(f"Error {Error}")

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    user_select = int(input("Enter a sign for the operation: "))

    if user_select == 1:
        print(f"{number1 + number2}")
    elif user_select == 2:
        print(f"{number1 - number2}")
    elif user_select == 3:
        print(f"{number1 * number2}")
    elif user_select == 4:
        print(f"{number1 / number2}")
    else:
        print("Incorrect input")

except ValueError as error:
    print("Please, enter an integer!")
    print(f"ValueError occurred: {error}")
except Exception as Error:
    print(f"Error {Error}")

