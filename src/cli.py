import argparse

from src.counter import regular_count

def run():
    parser = argparse.ArgumentParser(description="Word Frequency Analyzer")
    parser.add_argument('-f', dest='filename', help="Path to the text file for the analysis.")
    parser.add_argument('-w', action="append", dest='wordlist', default=[], help="Add a word to analyze.")

    args = parser.parse_args()
    print(args.filename)

    try:
        fileTmp = open(args.filename, 'r')
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")
        exit(1)
    
    print("\nFile \"" + args.filename + "\" opened for analysis...\n")

    for word in args.wordlist:
        print("Analyzing " + word + " ... ", end='')
        count = regular_count(word, fileTmp)
        print(count)

    fileTmp.close()