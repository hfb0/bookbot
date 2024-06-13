def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print(count_characteres(text))


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

main()