import argparse

import src.analysis as analysis

from src.log import PlainTextFileLogger
from src.log import CliLogger

def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    configure_switches(parser)

    args = parser.parse_args()

    # If the user specified an output filename
    if args.output_filename != None:
        try:
            output_file = open(args.output_filename, 'w')
        except FileNotFoundError:
            print("\nInvalid output file name: " + args.output_filename)
        logger = PlainTextFileLogger(output_file)
    else:
        logger = CliLogger()

    try:
        print("\nStarting Analysis...\n")
        analysis.analyze(args, logger)
    except FileNotFoundError as e:
        print("\nFile", e.filename , "not found. Please enter a valid filename.")
        exit(1)

    try:
        output_file.close()
        print('\nResults of the analysis were written in file ' + args.output_filename)
    except NameError:
        pass

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