def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("==============================================")
        print("--- Begin report of books/frankenstein.txt ---")
        print("==============================================")
        print(f"{count_words(file_contents)} words found in the book")
        print("------")
        count_characters(file_contents)
        print("------")
        print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_characters(text):
    character_dict = {}
    lower_text = text.lower()
    for letter in lower_text:
        # if ord(letter) >= 97 and ord(letter) <= 122:
        if letter not in character_dict:
            character_dict[letter] = 1
        elif letter in character_dict:
            character_dict[letter] += 1
    
    for character in character_dict:
        if ord(character) >= 97 and ord(character) <= 122:
            print(f"The '{character}' character was found {character_dict[character]} times")


main()