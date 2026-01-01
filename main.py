def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def main():
    get_book_text(books/frankenstein.txt)

main()