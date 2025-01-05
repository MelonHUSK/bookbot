import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_num = get_num_each_char(text)
    print(f"{num_words} words found in the document")
    print(f"Characters in document: {chars_num}")


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_each_char(text):
    words_lwr = text.lower()
    words_lwr = words_lwr.replace(" ", "")
    chars = list(words_lwr)
    chars_num = {}
    alphabet = string.ascii_lowercase

    for char in chars:
        if char in alphabet:  # Only count alphabetic characters
            if char in chars_num:
                chars_num[char] += 1
            else:
                chars_num[char] = 1
    
    return(chars_num)



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
