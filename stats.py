def sort_on(item):
	return item[1]

def char_dict_to_sorted_list(chars_dict):
	sorted_list = []
	for char in chars_dict:
		sorted_list.append((char,chars_dict[char]))
		sorted_list = sorted(sorted_list, key = sort_on, reverse = True)
	return sorted_list

def get_num_words(text):
	return len(text.split())

def get_num_chars(text):
	chars ={}
	for c in text.lower():
		if c in chars:
			chars[c]+= 1
		else:
			chars[c] = 1
	return chars

