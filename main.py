from stats import word_counter, char_counter, chars_to_sorted_list
import sys

def get_book_text(title_path):
    with open(title_path) as f:
        file_contents = f.read()
    return file_contents

def user_input():
    if len(sys.argv) != 2:
        raise Exception ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        location = sys.argv[1]
    return location

def main():
    text_location = user_input()
    text_full = get_book_text(text_location)
    count_dict = char_counter(text_full)
    sorted_list = chars_to_sorted_list(count_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counter(text_full)} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        if i["char"].isalpha() == True:
            print(f"{i["char"]}: {i["num"]} ")
    print("============= END ===============")


main()
