def main():
    book_path = "books/frankenstein.txt"
    print(f"---- Being report of {book_path} ----")
    print(get_word_count(book_path))
    print("\n")
    num_letters = get_letter_count(book_path)
    sorted_list = chars_dict_to_sorted_list(num_letters)
    for item in sorted_list:
        print(f"The {item['char']} character was found {item['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(path):
    text = get_book_text(path)
    words = text.split()
    return len(words)


def get_letter_count(path):
    text = get_book_text(path)
    num_letters = {}
    for letter in text:
        lowered = letter.lower()
        if lowered.isalpha():
            if lowered in num_letters:
                num_letters[lowered] += 1
            else:
                num_letters[lowered] = 1
    return num_letters

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()