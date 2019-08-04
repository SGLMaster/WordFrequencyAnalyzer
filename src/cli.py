import argparse

from src.counter import regular_count

def process_words(args, file):
    for word in args.wordlist:
        print("Analyzing " + word + " ... ", end='')
        count = regular_count(word, file)
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
    parser.add_argument('-i', action='store_true', default=False, dest='boolean_switch', 
                        help='Switch to activate the "Continous Present" -ing inflection.')

    args = parser.parse_args()
    analysis(args)