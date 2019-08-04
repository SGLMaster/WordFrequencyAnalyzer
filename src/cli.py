import argparse

import src.counter as counter
import src.inflection as infl

def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    configure_switches(parser)

    args = parser.parse_args()
    analysis(args)

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

def analysis(args):
    try:
        input_file = open(args.input_filename, 'r')
    except FileNotFoundError:
        print("Input file not found. Please enter a valid filename.")
        exit(1)

    try:
        output_file = open(args.output_filename, 'w')
    except FileNotFoundError:
        print("Output file not found. Please enter a valid filename.")
        exit(1)
    
    print("\nFile \"" + args.input_filename + "\" opened for analysis...\n")
    process_words(args, input_file, output_file)
    input_file.close()
    output_file.close()

def process_words(args, input_file, output_file):
    for word in args.wordlist:
        print("Analyzing " + word + " ... ", end='')
        count = counter.regular_count(word, input_file)

        if args.switch_ing:
            count += counter.regular_count(infl.inflect_ing(word), input_file)
        if args.switch_plural:
            count += counter.regular_count(infl.inflect_plural(word), input_file)
        if args.switch_past:
            count += counter.regular_count(infl.inflect_past(word), input_file)
        if args.switch_er:
            count += counter.regular_count(infl.inflect_er(word), input_file) 

        output_file.write(word + ":" + str(count) + "\n")

        print(count)