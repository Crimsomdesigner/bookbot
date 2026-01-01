def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def get_word_counts(File_text):
    counts = len(File_text.split())
    return counts

def main():
    file_path = 'books/frankenstein.txt'
    file_contents = get_book_text(file_path)
    num_words = get_word_counts(file_contents)
    print("Found {num_words} total words")
    
main()