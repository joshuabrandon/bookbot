import sys
from stats import count_words,count_characters,sorted_dict_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    #book_path = "books/frankenstein.txt"
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    sorted_list = sorted_dict_list(character_count)
    
    print(f"Analyzing book found at {book_path}...")
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_list:
        key = list(item.keys())[0]
        value = list(item.values())[0]
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

main()