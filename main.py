def main():
    book_path = "books/frankenstein.txt"
    print_report(book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_characteres(text):
    dict_count = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if(char in dict_count):
            dict_count[char] += 1
        else:
            dict_count[char] = 1

    return dict_count

def print_report(book_path):
    print(f"--- Begin report of {book_path} ---")

    text = get_book_text(book_path)

    count_w = count_words(text)
    print(f"{count_w} words found in the document \n")

    dict_c = count_characteres(text)
    lst_c = list(dict_c.items())
    lst_c.sort(reverse=True, key=sort_on_count)

    for character, count_c in lst_c:
        if(character.isalpha()):
            print(f"The '{character}' character was found {count_c} times")

    print("--- End report ---")

def sort_on_count(tuple):
    return tuple[1]

main()