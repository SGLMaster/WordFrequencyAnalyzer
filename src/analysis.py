import src.counter as counter
import src.inflection as infl

def analyze(args, logger):
    input_file = open(args.input_filename, 'r')
    process_file(args, input_file, logger)
    input_file.close()

def process_file(args, input_file, logger):
    for word in args.wordlist:
        process_word(word, args, input_file, logger)

def process_word(word, args, input_file, logger):
    count = counter.regular_count(word, input_file) # This is the default count without inflections
    logger.log(" " + word + ":" + str(count))

    total_count = count

    if args.switch_ing:
        total_count += get_inflected_count(word, infl.inflect_ing, input_file, logger)
    if args.switch_plural:
        total_count += get_inflected_count(word, infl.inflect_plural, input_file, logger)
    if args.switch_past:
        total_count += get_inflected_count(word, infl.inflect_past, input_file, logger)
    if args.switch_er:
        total_count += get_inflected_count(word, infl.inflect_er, input_file, logger)

    logger.log("--------------------------------------------------------------")
    logger.log(" Total:" + str(total_count) + "\n")

def process_word_in_multiple_files(word, args, input_files_list, logger):
    count = counter.multiple_files_count(word, input_files_list) # This is the default count without inflections
    logger.log(" " + word + ":" + str(count))

    total_count = count

    if args.switch_ing:
        total_count += get_inflected_count(word, infl.inflect_ing, input_files_list, logger)
    if args.switch_plural:
        total_count += get_inflected_count(word, infl.inflect_plural, input_files_list, logger)
    if args.switch_past:
        total_count += get_inflected_count(word, infl.inflect_past, input_files_list, logger)
    if args.switch_er:
        total_count += get_inflected_count(word, infl.inflect_er, input_files_list, logger)

    logger.log("--------------------------------------------------------------")
    logger.log(" Total:" + str(total_count) + "\n")

def get_inflected_count(word, inflection_func, input_files_list, logger):
    inflected_word = inflection_func(word)
    count = counter.multiple_files_count(inflected_word, input_files_list)
    logger.log("+" + inflected_word + ":" + str(count))
    return count