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