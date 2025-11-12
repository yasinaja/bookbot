def get_num_words(text):
        text_list = text.split()
        num_words = len(text_list)
        return f"Found {num_words} total words"

def get_num_chars(text):
	text_lower = text.lower()
	num_char_dict = {}

	for char in text_lower:
		if not char.isalpha():
			continue
		elif char in num_char_dict:
			num_char_dict[char] += 1
		else:
			num_char_dict[char] = 1
	
	return num_char_dict

def get_text_dict_sorted(text_dict):
	text_dict_sorted = dict(sorted(text_dict.items(), key=lambda item: item[1], reverse=True))

	text = ""
	for k,v in text_dict_sorted.items():
		text += f"{k}: {v}\n"
	
	return text


def get_report(file_path, num_words, text_dict):
	return f"""
============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{text_dict}
============= END ===============
"""
