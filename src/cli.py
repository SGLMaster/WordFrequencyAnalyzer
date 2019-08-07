import argparse

import src.analysis as analysis

from src.log import PlainTextFileLogger
from src.log import CliLogger

def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    configure_switches(parser)

    args = parser.parse_args()
    assert_arguments(args)
    logger = get_logger(args)

    try_to_analyze(args, logger)

def configure_switches(parser):
    parser.add_argument('-f', action="append", dest='input_filenames', default=[], 
                        help="Path to the text file to analyze.")
    parser.add_argument('-o', dest='output_filename', help="Path to the output text file to dump the results.")
    parser.add_argument('-w', action="append", dest='wordlist', default=[], help="Add a word to analyze.")
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

def get_logger(args):
    # If the user specified an output filename
    if args.output_filename != None:
        try:
            output_file = open(args.output_filename, 'w')
        except FileNotFoundError:
            print("\nInvalid output filename: " + args.output_filename)
        return PlainTextFileLogger(output_file)
    
    return CliLogger()

def try_to_analyze(args, logger):
    try:
        print("\nStarting Analysis...\n")

        word_list = args.wordlist
        input_files_list = []

        for filename in args.input_filenames:
            input_file = open(filename, 'r', encoding="utf8")
            input_files_list.append(input_file)

        for word in word_list:
            analysis.process_word_in_multiple_files(word, args, input_files_list, logger)

        print("\nAnalysis completed succesfully\n")

        if logger is PlainTextFileLogger:
            logger.close()

    except FileNotFoundError as e:
        print("\nFile" + e.filename + "not found. Please enter a valid filename.")
        exit(1)