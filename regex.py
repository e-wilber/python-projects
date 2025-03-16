"""
* Name         : regex.py
* Author       : E Wilber
* Created      : 01/27/25
* Module       : 2
* Topic        : 3
* Description  : Regexing Assignment
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import re
passage = (
    "“I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. "
    "I will face my fear. I will permit it to pass over me and through me. And when it has gone past I "
    "will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain.” "
    "– Frank Herbert, Dune"
)
# Regex
f_containing_words = re.findall(r'\b\w*[fF]\w*\b', passage)
f_starting_words = re.findall(r'\b[fF]\w*\b', passage)
not_whole_word = re.findall(r'\bnot\b', passage, re.IGNORECASE)
# Counts occurrences
count_f_containing_words = len(f_containing_words)
count_f_starting_words = len(f_starting_words)
count_not = len(not_whole_word)
# Updates passage
updated_passage = re.sub(r'\bI\b', 'You', passage)
updated_passage = re.sub(r'\bmy\b', 'your', updated_passage)
updated_passage = re.sub(r'\bme\b', 'you', updated_passage)
# Print results
print("How many words contain the letter f: ", count_f_containing_words)
print("How many words start with the letter f: ", count_f_starting_words)
print("How many times the word 'not' appears: ", count_not)
print("\nUpdated Passage: ")
print(updated_passage)
