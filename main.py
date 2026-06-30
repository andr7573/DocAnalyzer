import sys
from readers import read_document
from stats import get_num_words, get_num_chars, char_dict_to_sorted_list

def print_report(path, num_words, sorted_chars):
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char, count in sorted_chars:
                if char.isalpha():
                        print(f"{char}: {count}")
        print("============= END ===============")

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	path = sys.argv[1]
	text = read_document(path)
	
	num_words = get_num_words(text)
	num_chars = get_num_chars(text)

	sorted_chars = char_dict_to_sorted_list(num_chars)
	print_report(path,num_words, sorted_chars)

main() 
