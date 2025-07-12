from stats import count_words, analyze_book
import sys

try:
    input_path = sys.argv[1]
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    exit(1)

count_words(input_path)
analyze_book(input_path)
