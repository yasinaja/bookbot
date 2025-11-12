from stats import get_num_words, get_num_chars, get_text_dict_sorted, get_report
import sys


def get_book_text(file_path):
        with open(file_path) as f:
                file_contents = f.read()
        return file_contents

def main():
        if len(sys.argv) != 2:
                print("Usage: python3 main.py <path_to_book>")
                sys.exit(1)
        else:
                file_path = sys.argv[1]
        
        book_text = get_book_text(file_path)
        num_words = get_num_words(book_text)
        text_dict = get_text_dict_sorted(get_num_chars(book_text))
        report = get_report(file_path, num_words, text_dict)
        print(report)

main()