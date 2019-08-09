import src.counter as counter
import src.inflection as infl


def process_word(word, args, filenames, logger):
    # This is the default count without inflections
    count = counter.multiple_files_count(word, filenames)
    logger.log(" " + word + ":" + str(count))

    total_count = count

    if args.switch_ing:
        total_count += get_inflected_count(word,
                                           infl.inflect_ing, filenames, logger)
    if args.switch_plural:
        total_count += get_inflected_count(word,
                                           infl.inflect_plural, filenames, logger)
    if args.switch_past:
        total_count += get_inflected_count(word,
                                           infl.inflect_past, filenames, logger)
    if args.switch_er:
        total_count += get_inflected_count(word,
                                           infl.inflect_er, filenames, logger)

    logger.log("--------------------------------------------------------------")
    logger.log(" Total:" + str(total_count) + "\n")


def get_inflected_count(word, inflection_func, filenames, logger):
    inflected_word = inflection_func(word)
    count = counter.multiple_files_count(inflected_word, filenames)
    logger.log("+" + inflected_word + ":" + str(count))
    return count
