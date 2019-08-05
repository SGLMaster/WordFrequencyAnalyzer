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
    parser.add_argument('-f', dest='input_filename', help="Path to the text file to analyze.")
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
    if args.input_filename == None:
        print("\nPlease enter the name of the file to analyze.")
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
        analysis.analyze(args, logger)
        print("\nAnalysis completed succesfully\n")

        if logger is PlainTextFileLogger:
            logger.close()
    except FileNotFoundError as e:
        print("\nFile" + e.filename + "not found. Please enter a valid filename.")
        exit(1)