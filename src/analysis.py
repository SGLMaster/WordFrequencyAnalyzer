import src.counter as counter
import src.inflection as infl
from src.counter import WordCount


def process_word(word, args, filenames):
    # This is the default count without inflections
    count = counter.get_word_count(word, filenames)

    word_counter = WordCount(word)
    word_counter.set_normal_count(count)
    #total_count = count

    
    if args.switch_ing:
        word_counter.set_ing_count(get_inflected_count(word, infl.inflect_ing, filenames))
    if args.switch_plural:
        word_counter.set_plural_count(get_inflected_count(word, infl.inflect_plural, filenames))
    if args.switch_past:
        word_counter.set_past_count(get_inflected_count(word, infl.inflect_past, filenames))
    if args.switch_er:
        word_counter.set_er_count(get_inflected_count(word, infl.inflect_er, filenames))

    return word_counter


def get_inflected_count(word, inflection_func, filenames):
    inflected_word = inflection_func(word)
    count = counter.get_word_count(inflected_word, filenames)
    return count
