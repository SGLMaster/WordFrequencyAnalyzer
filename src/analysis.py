import src.counter as counter
import src.inflection as infl

def analyze(args, logger):
    input_file = open(args.input_filename, 'r')
    process_words(args, input_file, logger)
    input_file.close()

def process_words(args, input_file, logger):
    for word in args.wordlist:
        count = counter.regular_count(word, input_file) # This is the default count without inflections
        total_count = count

        logger.log(" " + word + ":" + str(count))

        if args.switch_ing:
            word_ing = infl.inflect_ing(word)
            count_ing = counter.regular_count(word_ing, input_file)
            logger.log("+" + word_ing + ":" + str(count_ing))
            total_count += count_ing
        if args.switch_plural:
            word_plural = infl.inflect_plural(word)
            count_plural = counter.regular_count(word_plural, input_file)
            logger.log("+" + word_plural + ":" + str(count_plural))
            total_count += count_plural
        if args.switch_past:
            word_past = infl.inflect_past(word)
            count_past = counter.regular_count(word_past, input_file)
            logger.log("+" + word_past + ":" + str(count_past))
            total_count += count_past
        if args.switch_er:
            word_er = infl.inflect_er(word)
            count_er = counter.regular_count(word_er, input_file)
            logger.log("+" + word_er + ":" + str(count_er))
            total_count += count_er

        logger.log("----------------------------------------------------------------")
        logger.log(" Total:" + str(total_count) + "\n")