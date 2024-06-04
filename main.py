def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)

    n_words = count_words(text)
    di = count_characters(text)
    li = dict_to_sorted_list(di)

    print(f"--- Begin report of {path} ---")
    print(f"{n_words} words found in the document")
    for d in li:
        if d['char'].isalpha():
            print(f"The {d['char']} character was found {d['num']} times")
    print("--- End report ---")

def get_book_text(path):
        with open("./" + path) as f:
            file_contents = f.read()
        return file_contents

def count_words(string):
    words = string.split()
    count = len(words)
    return count

def count_characters(string):
    string = string.lower()
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    li = []
    for key, value in dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        li.append(new_dict)
        li.sort(reverse=True, key=sort_on)
    return li


def print_report(file):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(file)} words found in the document.")
    character_count = count_characters(file)
    character_count.sort()
    for char in character_count:
        if char.isalpha():
            print(f"The '{char}' character was found {character_count[char]} times")

    print("--- End report ---")
main()