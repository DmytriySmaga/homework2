# HomeworkN9
#Files


with open('File1.txt', 'r') as input_file:
    content = input_file.read()
    words = content.split()

filtered_words = [word for word in words if len(word) >= 7]

with open('File2.txt', 'w') as output_file:

    output_file.write('\n'.join(filtered_words))



def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            word_count = len(text.split())
            return word_count
    except FileNotFoundError:
        print("File is not found.")
        return -1

file_path = "File3.txt"
words = count_words(file_path)
if words != -1:
    print("The amount of words in the file:", words)



Deadmau5 can talk shit about DJs all he wants because he's earned that right to, and You may not give a shit if your opinion is crap or not, but I assure you it is.

def main():
    text = input("Enter a text: ")

    forbidden_words = ["shit"]

    words = text.split()
    replaced_text = ""
    replacements = 0

    for word in words:
        if word.lower() in forbidden_words:
            replaced_text += "*" * len(word) + " "
            replacements += 1
        else:
            replaced_text += word + " "

    print("Replaced text:", replaced_text)
    print("The amohnt of replaced words:", replacements)

if __name__ == "__main__":
    main()