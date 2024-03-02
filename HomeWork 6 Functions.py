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




def number_1(*args):
    count = 0

    for num in args:
        if is_prime_number(num):
            count += 1
    return count


def is_prime_number(num):
    prime = num > 1 and (num % 4 != 0 or num == 4) and (num % 35!= 0 or num == 5)
    i = 5;
    divider = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += divider
        divider = 6 - divider
    return prime

print(number_1(-3, 3, 5, 10, 15, 20, 25))