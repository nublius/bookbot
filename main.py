import sys
from stats import get_num_words, get_char_count, get_char_dicts

if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

def get_book_text(file):
    with open(file) as f:
        return f.read()

def pretty_print(book):
    book_filepath = book
    book_text = get_book_text(book)
    word_num = get_num_words(book_text)
    char_count = get_char_count(book_text)
    char_dicts = get_char_dicts(char_count)

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_filepath}...')
    print('----------- Word Count ----------')
    print(f'Found {word_num} total words')
    print('--------- Character Count -------')
    for item in char_dicts:
        print(f'{item["char"]}: {item["num"]}')
    print('============= END ===============')

pretty_print(sys.argv[1])
