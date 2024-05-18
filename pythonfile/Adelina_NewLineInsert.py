import re

def insert_newline_before_word(filename, word):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            # Remove numbers followed by ");" before "Insert"
            line = re.sub(r'(\d+\);)\s*Insert', r'Insert', line)
            # Add new line before "Insert"
            line = line.replace(word, '\n' + word)
            file.write(line)

# Example usage:
filename = 'RULE_AND_RULE_PREDICATE.sql'
word_to_search = 'Insert'
insert_newline_before_word(filename, word_to_search)
