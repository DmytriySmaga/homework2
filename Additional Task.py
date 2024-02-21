# Additional Task
# Number one

text1 = "it was Teddy's day-off, on Sunday!"
print(text1.capitalize())
text2 = "he went to the park, that's 200m away from his home!"
print(text2.capitalize())
text3 = "he had some coffee, cappuccino for the cost of 2.49$."
print(text3.capitalize())
text4 = "it was a really, really great day!!"
print(text4.capitalize())

digit_count = 0

for number in text1:
    if number.isdigit():
        digit_count += 1

for number in text2:
    if number.isdigit():
        digit_count += 1

for number in text3:
    if number.isdigit():
        digit_count += 1

for number in text4:
    if number.isdigit():
        digit_count += 1
print('Number of digits:', digit_count)

symbol_count = 0

for symbol in text1:
    if "," == symbol:
        symbol_count += 1
    elif "." == symbol:
        symbol_count += 1

for symbol in text2:
    if "," == symbol:
        symbol_count += 1
    elif "." == symbol:
        symbol_count += 1

for symbol in text3:
    if "," == symbol:
        symbol_count += 1
    elif "." == symbol:
        symbol_count += 1

for symbol in text4:
    if "," == symbol:
        symbol_count += 1
    elif "." == symbol:
        symbol_count += 1

print('Number of symbols:', symbol_count)

exclamations_count = 0

for exclamations in text1:
    if "!" == exclamations:
        exclamations_count += 1

for exclamations in text2:
    if "!" == exclamations:
        exclamations_count += 1

for exclamations in text3:
    if "!" == exclamations:
        exclamations_count += 1

for exclamations in text4:
    if "!" == exclamations:
        exclamations_count += 1

print('Number of exclamations:', exclamations_count)