from util import get_file_from_cli, create_phrases, generate_message
import sys
import time


def main():
    """
    Improvements:
        - it would be better to handle exceptions in each function
    """
    start_time = time.perf_counter()

    try:
        file_to_search = get_file_from_cli(sys.argv[1])
    except Exception as e:
        print("failed cli args", e, sep="\n")

    try:
        search_me = open(file_to_search, "r")
    except Exception as e:
        print("failed file open", e, sep="\n")

    try:
        three_word_phrases = create_phrases(search_me, 3)
    except Exception as e:
        print("failed phrase creation", e, sep="\n")

    try:
        generate_message(three_word_phrases, 100)
    except Exception as e:
        print("failed message generation", e, sep="\n")

    search_me.close()
    end_time = time.perf_counter()
    print("Total Time: ", f"{end_time - start_time} seconds")
    return


if __name__ == "__main__":
    main()
