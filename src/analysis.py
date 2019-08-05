import src.counter as counter
import src.inflection as infl

def analyze(args):
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
        raise

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