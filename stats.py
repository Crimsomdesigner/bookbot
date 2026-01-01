def get_word_counts(File_text):
    counts = len(File_text.split())
    return counts

def get_char_counts(File_text):
    t_count = 0
    p_count = 0
    c_count = 0
    char_list = list(File_text.lower())
    for c in range(0, len(char_list)):
        if char_list[c] == "t":
            t_count += 1
        elif char_list[c] == "p":
            p_count += 1
        elif char_list[c] == "c":
            c_count += 1
    return {
        "t": t_count,
        "p": p_count,
        "c": c_count,
    }
    