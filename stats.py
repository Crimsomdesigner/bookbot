def get_word_counts(File_text):
    counts = len(File_text.split())
    return counts

def get_char_counts(File_text):
    char_dict = {}
    char_list = list(File_text.lower())
    for character in char_list:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    return char_dict
    