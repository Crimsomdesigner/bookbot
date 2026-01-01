def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

from stats import get_word_counts
from stats import get_char_counts

def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    num_words = get_word_counts(file_contents)
    f_string = f"Found {num_words} total words"
    print(f_string)
    print(get_char_counts(file_contents))

main()