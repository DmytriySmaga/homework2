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




user_prints = int(input("Please, enter any number: "))
def print_stars(n):

    if n <= 0:

        return

    print('*', end=" ")

    print_stars(n-1)
#
print_stars(user_prints)
