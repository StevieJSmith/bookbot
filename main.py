def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)
        print("------")
        count_characters(file_contents)

def count_words(text):
    print(len(text.split()))

def count_characters(text):
    character_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        # if ord(letter) >= 97 and ord(letter) <= 122:
        if letter not in character_dict:
            character_dict[letter] = 1
        elif letter in character_dict:
            character_dict[letter] += 1
    print(character_dict)


main()