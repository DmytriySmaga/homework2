#HomeWork7
#Recursion


def my_power(number, power):
    if power <= 1:
        return number

    return number * my_power(number, power - 1)

print(my_power(5, 5))

# my_power(5, 5) -> 5 * my_power(5, 4) -> 3125
# my_power(5, 4) -> 5 * my_power(5, 3) -> 625
# my_power(5, 3) -> 5 * my_power(5, 2) -> 125
# my_power(5, 2) -> 5 * my_power(5, 1) -> 25
# my_power(5, 1) -> 5
