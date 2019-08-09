import argparse

import src.analysis as analysis


def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    configure_switches(parser)

    args = parser.parse_args()
    assert_arguments(args)

    try_to_analyze(args)


def configure_switches(parser):
    parser.add_argument('-f', action="append", dest='input_filenames', default=[],
                        help="Path to the text file to analyze.")
    parser.add_argument('-o', dest='output_filename',
                        help="Path to the output text file to dump the results.")
    parser.add_argument('-w', action="append", dest='wordlist',
                        default=[], help="Add a word to analyze.")
    parser.add_argument('-i', action='store_true', default=False, dest='switch_ing',
                        help='Switch to activate the "Continous Present" -ing inflection.')
    parser.add_argument('-s', action='store_true', default=False, dest='switch_plural',
                        help='Switch to activate the "Plural" -s or -es inflection.')
    parser.add_argument('-p', action='store_true', default=False, dest='switch_past',
                        help='Switch to activate the "Past" -ed or -d inflection.')
    parser.add_argument('-e', action='store_true', default=False, dest='switch_er',
                        help='Switch to activate the -er or -r inflection.')


def assert_arguments(args):
    if len(args.input_filenames) == 0:
        print("\nPlease enter at least one file to analyze.")
        exit(1)
    elif len(args.wordlist) == 0:
        print("\nPlease enter at least one word to search.")
        exit(1)


def try_to_analyze(args):
    try:
        print("\nStarting Analysis...\n")

        word_list = args.wordlist
        for word in word_list:
            word_count = analysis.process_word(
                word, args, args.input_filenames)
            word_count.log(args)

        print("\nAnalysis completed succesfully\n")

    except FileNotFoundError as e:
        print("\nFile" + e.filename + "not found. Please enter a valid filename.")
        exit(1)
