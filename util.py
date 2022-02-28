import string
from collections import Counter
from pathlib import Path


def get_file_from_cli(cli_input):
    """
    Desc: search cli arguments, get name/path of filename that is inputted
    Returns: a path for the file, or an error
    Bugs:
    """
    filename = cli_input
    file_path = Path(__file__).parent / "texts" / f"{filename}"
    if file_path.exists():
        return file_path
    else:
        error_string = f"sorry, {file_path} does not exist"
        print(error_string)
        return error_string


def create_phrases(file_to_read, num_words_per_phrase):
    """
    Desc: search file line-by-line and make a list phrases from consecutive words
    Returns: a list of lowercase phrases without punctuation
    Bugs:
        - This is dependent on the apostrophe-type used in the text
            - this removes ' but not ’ so "John's" becomes "Johns" but might not
                but "John’s" remains unchanged
            - "won't" may also become "wont", which are two distinct but legitimate words
        - `string.punctuation` is useful but does not address line-endings, such as hyphen-
            ated breaks
            - "hyphen-\nated" will become ["hyphen", "ated"]
            - this could be addressed by conditionally searching line-endings for hyphens
    """

    words = []
    for line in file_to_read:
        # make a table of string replacements
        # replace everything in the line that matches `string.punctuation` list with blank strings
        filtered = line.translate(str.maketrans("", "", string.punctuation))
        words_in_line = filtered.lower().split()
        for word in words_in_line:
            # can this be list comprehension instead?
            # TODO: search words_in_line for hyphenated line-endings
            words.append(word)

    phrases = []
    for i in range(len(words) - (num_words_per_phrase - 1)):
        # we subtract (num_words_per_phrase - 1) since the indices of the words
        #   list end at <max i + (num_words_per_phrase - 1)>
        # make a (num_words_per_phrase - 1) word phrase that iterates per word
        phrases.append(f"{words[i]} {words[i + 1]} {words[i + 2]}")

    return phrases


def generate_message(some_phrases, num_phrases):
    """
    Desc: return a message for each phrase in `some_phrases` with a quantity
    Bugs: `most_often` is allowed to be zero or exceptionally long
    """
    count = Counter(some_phrases)
    most_often = count.most_common(num_phrases)
    for phrase in most_often:
        print(f"{phrase[0]} - {phrase[1]}")
    return
