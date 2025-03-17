from stats import count_words
from stats import count_characters
from stats import char_count_sorted
import sys

def get_book_text(filepath):
    text=""
    with open(filepath) as f:
        text = f.read()

    return text

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    num_chars = count_characters(book)
    #print(f"{num_words} words found in the document")
    #print(num_chars)
    list_sorted=char_count_sorted(num_chars)
    #print(list_sorted)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/book.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in list_sorted:
        if char["character"].isalpha():
            print(f"{char["character"]}: {char["count"]}")
    print("============= END ===============")

main()