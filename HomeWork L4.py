#Lesson4
#strings

# try:
#     user_writes = input("Please, enter any line: ")
#
# except Exception as Error:
#     print(f"Error {Error}")
#
# letter_count = 0
# digit_count = 0
#
# for letter in user_writes:
#    if letter.isalpha():
#        letter_count += 1
#
#    elif letter.isdigit():
#        digit_count += 1
#
# print('Number of letters:', letter_count)
# print('Number of digits:', digit_count)

# line = input("Please, type anything you want: ")
# letter = input("Enter a symbol to be found: ")
#
# count = 0
# for n in line:
#     if n == letter:
#
#        count += 1
#
#        print(f"Symbol {letter} appears {count} times in the sentence")


# user_text = input("Say hello to your friends and get it in Spanish: ")
# symbol = input("Enter a character to search for: ")
# print(user_text)
#
# count = 0
# for l in user_text:
#     if l == symbol:
#
#         count += 1
#
#         print(f"Character {symbol} appears {count} times in the sentence")
#
# text = user_text.replace(f"{user_text}", "¡Hola amigos!", 1)
# print(text)


text = "What a beautiful morning"
print(text[2:4:23])

print(text[22:24])

print(text[:5])

print(text[:22])

print(text[1::2])

print(text[::2])

print(text[::-1])

print(text[-1:0:-2])

print(text[:])
print(len(text))