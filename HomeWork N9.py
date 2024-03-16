# HomeworkN9
#Files


with open('File1.txt', 'r') as input_file:
    content = input_file.read()
    words = content.split()

filtered_words = [word for word in words if len(word) >= 7]

with open('File2.txt', 'w') as output_file:

    output_file.write('\n'.join(filtered_words))