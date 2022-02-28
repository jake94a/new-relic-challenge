import sys
import string
import time
from collections import Counter

start_time = time.perf_counter()

filename_to_search = sys.argv[1]
textfile_path = f"{sys.path[0]}/texts/{filename_to_search}"

file_to_search = open(textfile_path, "r")
words = []

for line in file_to_search:
    # this removes ' but not ’ so John's could become Johns
    # won't may also becomes wont, which are two different (but legitimate) words
    # This is a bug and is dependent on the apostrophe-type used in the text
    filtered = line.translate(str.maketrans("", "", string.punctuation))
    words_in_line = filtered.lower().split()
    for word in words_in_line:
        # can this be list comprehension instead?
        words.append(word)

three_word_phrases = []
for i in range(len(words) - 2):
    # we subtract 2 since the indices of the words list end at <max i + 2>
    # make a three word phrase that iterates per word
    three_word_phrases.append(f"{words[i]} {words[i + 1]} {words[i + 2]}")


Counter = Counter(three_word_phrases)

most_often = Counter.most_common(100)
print("most_often", most_often)

end_time = time.perf_counter()

print("Total Time: ", f"{end_time - start_time} seconds")
