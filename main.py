def get_book_text(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def main():
    file_path = 'books/frankenstein.txt'
    File_contents = get_book_text(file_path)
    print (File_contents)
main()