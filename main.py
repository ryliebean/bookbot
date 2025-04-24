from stats import word_counter, char_counter

def get_book_text(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    word_count = word_counter(get_book_text("books/frankenstein.txt"))
    char_count = char_counter(get_book_text("books/frankenstein.txt"))
    print(f"{word_count} words found in the document")
    print(char_count)

main()
