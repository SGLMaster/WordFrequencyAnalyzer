import argparse

import src.counter as counter
import src.inflection as infl

def process_words(args, file):
    for word in args.wordlist:
        print("Analyzing " + word + " ... ", end='')
        count = counter.regular_count(word, file)

        if args.switch_ing:
            count += counter.regular_count(infl.inflect_ing(word), file)
        if args.switch_plural:
            count += counter.regular_count(infl.inflect_plural(word), file)
        if args.switch_past:
            count += counter.regular_count(infl.inflect_past(word), file)
        if args.switch_er:
            count += counter.regular_count(infl.inflect_er(word), file) 

        print(count)

def analysis(args):
    try:
        fileTmp = open(args.filename, 'r')
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
        exit(1)
    
    print("\nFile \"" + args.filename + "\" opened for analysis...\n")
    process_words(args, fileTmp)
    fileTmp.close()

def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    parser.add_argument('-f', dest='filename', help="Path to the text file for the analysis.")
    parser.add_argument('-w', action="append", dest='wordlist', default=[], help="Add a word to analyze.")
    parser.add_argument('-i', action='store_true', default=False, dest='switch_ing', 
                        help='Switch to activate the "Continous Present" -ing inflection.')
    parser.add_argument('-s', action='store_true', default=False, dest='switch_plural', 
                        help='Switch to activate the "Plural" -s or -es inflection.')
    parser.add_argument('-p', action='store_true', default=False, dest='switch_past', 
                        help='Switch to activate the "Past" -ed or -d inflection.')
    parser.add_argument('-e', action='store_true', default=False, dest='switch_er', 
                        help='Switch to activate the -er or -r inflection.')

    args = parser.parse_args()
    analysis(args)