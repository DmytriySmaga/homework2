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

line = input("Please, type anything you want: ")
letter = input("Enter a symbol to be found: ")

count = 0
for n in line:
    if n == letter:

       count += 1

       print(f"Symbol {letter} appears {count} times in the sentence")