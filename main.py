import sys

from stats import count_words
from stats import count_chars
from stats import sort_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        num_words = count_words(file_contents)
        sorted_char_totals = sort_chars(count_chars(file_contents))
        print("============ BOOKBOT =============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count -----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count --------")
        for d in sorted_char_totals:
            if d["char"].isalpha():
                s = d["char"] + ":"
                print(s, d["num"])
        print("============== END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_book_text(sys.argv[1])

main()
