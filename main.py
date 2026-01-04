import sys

def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

from stats import *

def main():
    #file_path =
    #file_contents = get_book_text(file_path)
    #num_words = get_word_counts(file_contents)
    #character_count_dict = get_char_counts(file_contents)
    #char_sorted_list = sort_on(character_count_dict)
    #print("============ BOOKBOT ============")
    #print(f"Analyzing book found at {file_path}...")
    #print("----------- Word Count ----------")
    #print(f"Found {num_words} total words")
    #print("--------- Character Count -------")
    #for d in char_sorted_list:
        #for char, count in d.items():
            #print(f"{char}: {count}")
    #print("============= END ===============")
    print(sys.argv)

main()