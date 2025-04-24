# File that contains functions for analyzing the text

def word_counter(word_string):
    count = 0
    for words in word_string.split():
        count += 1
    return count