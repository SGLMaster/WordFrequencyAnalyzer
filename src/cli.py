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
    input_file = try_get_file(args.input_filename, 'r')
    output_file = try_get_file(args.output_filename, 'w')
    
    print("\nFile \"" + args.input_filename + "\" opened for analysis...\n")
    process_words(args, input_file, output_file)
    input_file.close()
    output_file.close()

def try_get_file(filename, mode):
    try:
        return open(filename, mode)
    except FileNotFoundError:
        print("File", filename, "not found. Please enter a valid filename.")
        exit(1)

def process_words(args, input_file, output_file):
    for word in args.wordlist:
        print("Analyzing " + word + " ... ", end='')

        count = counter.regular_count(word, input_file) # This is the default count without inflections
        output_file.write(" " + word + ":" + str(count) + "\n")

        total_count = count

        if args.switch_ing:
            word_ing = infl.inflect_ing(word)
            count_ing = counter.regular_count(word_ing, input_file)
            output_file.write("+" + word_ing + ":" + str(count_ing) + "\n")
            total_count += count_ing
        if args.switch_plural:
            word_plural = infl.inflect_plural(word)
            count_plural = counter.regular_count(word_plural, input_file)
            output_file.write("+" + word_plural + ":" + str(count_plural) + "\n")
            total_count += count_plural
        if args.switch_past:
            word_past = infl.inflect_past(word)
            count_past = counter.regular_count(word_past, input_file)
            output_file.write("+" + word_past + ":" + str(count_past) + "\n")
            total_count += count_past
        if args.switch_er:
            word_er = infl.inflect_er(word)
            count_er = counter.regular_count(word_er, input_file)
            output_file.write("+" + word_er + ":" + str(count_er) + "\n")
            total_count += count_er

        print(total_count)
        output_file.write("----------------------------------------------------------------\n")
        output_file.write(" Total:" + str(total_count) + "\n\n")