# File that contains functions for analyzing the text

def word_counter(word_string):
    count = 0
    for words in word_string.split():
        count += 1
    return count

def char_counter(word_string):
    char_list = {}
    word_string.split()
    for char in word_string.lower():
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list