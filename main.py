def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_words(file_contents)

def count_words(text):
    print(len(text.split()))


main()