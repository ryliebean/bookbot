def get_book_text(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    print(get_book_text("books/frankenstein.txt"))


main()
