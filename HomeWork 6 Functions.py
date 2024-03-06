#HomeWork6


def multi(number1, number2, number3):
    return number1 * number2 * number3

def calculate() -> None:
    first_number = 2
    second_number = 4
    third_number = 6
    math_operation = "*"

    match math_operation:
        case "*":
            print(f"{first_number} {math_operation} {second_number} {math_operation} {third_number}"
                  f" = {multi(first_number, second_number, third_number)}")
        case _:
            raise Exception("Invalid math operation!")

try:
    calculate()
except Exception as error:
    print(error)
#



def minimal(num1, num2, num3):
    return min(num1), min(num2), min(num3)

def minimal() -> None:
    first_num = 22
    second_num = 11
    third_num = 44

    if first_num < second_num < third_num:
        print(first_num)
    elif first_num > second_num < third_num:
        print(second_num)
    elif first_num > second_num > third_num:
        print(third_num)

try:
    minimal()
except Exception as error:
    print(error)



import random


def is_prime(number: int) -> bool:
    is_number_prime = True

    for num in range(2, number):
        if number % num == 0:
            is_number_prime = False
            break

    return is_number_prime


def get_prime_numbers(numbers: list[int]) -> int:
    prime_numbers_counter = 0

    for num in numbers:
        if is_prime(num):
            print(num, end=" ")
            prime_numbers_counter += 1

    print()
    return prime_numbers_counter


my_numbers = [random.randint(1, 20) for _ in range(10)]
print(my_numbers)
result = get_prime_numbers(my_numbers)
print(f"Prime numbers count: {result}")



def delete_item(numbers: list[int], number: int) -> int:
    deleted_item_counter = 0

    for item in numbers:
        if item == number:
            numbers.remove(item)
            deleted_item_counter += 1

    return deleted_item_counter


nums = [1, 3, 1, 5, 2, 6, 1, 3, 2, 5]
print(nums)
result = delete_item(nums, 1)
print(result)
print(nums)




def two_lists(list1, list2):
    combined = list1 + list2

    return combined

list1 = [2, 4, 6, 8, 10]
list2 = [3, 5, 7, 9, 11]

merged_lists = two_lists(list1, list2)
print(merged_lists)



def powered_list(list, power):

 result = []

 for x in list:

   result.append(x**power)

 return result

nums = [2, 4, 6, 10]
powered_nums = powered_list(nums, 3)
print(powered_nums)
