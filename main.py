from stats import word_counter

def get_book_text(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    #x = word_counter("hello from word counter")
    x = word_counter(get_book_text("books/frankenstein.txt"))
    print(f"{x} words found in the document")


main()
