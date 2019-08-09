import pronouncing
import src.irregular as irregular


def get_syllable_count(word):
    pronunciation_list = pronouncing.phones_for_word(word)

    try:
        syllable_count = pronouncing.syllable_count(pronunciation_list[0])
    except IndexError:
        syllable_count = 0

    return syllable_count


def is_final_syllable_stressed(word):
    phones_list = pronouncing.phones_for_word(word)
    stresses = pronouncing.stresses(phones_list[0])

    if(stresses[-1] == '1'):
        return True

    return False


def is_vowel(character):
    if character.lower() in ('aeiou'):
        return True
    return False


def is_consonant(character):
    if character.lower() in ('bcdfghjklmnñpqrstvwxyz'):
        return True
    return False


def inflect_ing(word):
    if word.endswith('e') and not word.endswith('ee') and not word.endswith('ie'):
        wordInflected = word[:-1] + 'ing'
    elif word.endswith('ie'):
        wordInflected = word[:-2] + 'ying'
    elif get_syllable_count(word) == 1 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        # This is for cases with one syllable like "eat"
        if len(word) >= 3 and is_vowel(word[-3]):
            wordInflected = word + 'ing'
        else:
            wordInflected = word + word[-1] + 'ing'
    elif get_syllable_count(word) == 2 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        if is_final_syllable_stressed(word):
            wordInflected = word + word[-1] + 'ing'
        else:
            wordInflected = word + 'ing'
    else:
        wordInflected = word + 'ing'

    return wordInflected


def inflect_plural(word):
    if word in irregular.plurals.keys():
        wordInflected = irregular.plurals[word]
    elif word.endswith('s') or word.endswith('ss') or word.endswith('sh') or word.endswith('ch') or word.endswith('x') or word.endswith('o'):
        wordInflected = word + 'es'
    elif word.endswith('y') and len(word) >= 2 and is_consonant(word[-2]):
        wordInflected = word[:-1] + 'ies'
    else:
        wordInflected = word + 's'

    return wordInflected


def inflect_past(word):
    if word in irregular.past_participles.keys():
        wordInflected = irregular.past_participles[word]
    elif word.endswith('e'):
        wordInflected = word + 'd'
    elif word.endswith('y') and len(word) >= 2 and is_consonant(word[-2]):
        wordInflected = word[:-1] + 'ied'
    elif get_syllable_count(word) == 1 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        # This is for cases with one syllable like "wait"
        if len(word) >= 3 and is_vowel(word[-3]):
            wordInflected = word + 'ed'
        else:
            wordInflected = word + word[-1] + 'ed'
    elif get_syllable_count(word) == 2 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        if is_final_syllable_stressed(word):
            wordInflected = word + word[-1] + 'ed'
        else:
            wordInflected = word + 'ed'
    else:
        wordInflected = word + "ed"
    return wordInflected


def inflect_er(word):
    if word.endswith('e'):
        wordInflected = word + 'r'
    elif word.endswith('y') and len(word) >= 2 and is_consonant(word[-2]):
        wordInflected = word[:-1] + 'ier'
    elif get_syllable_count(word) == 1 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        # This is for cases with one syllable like "wait"
        if len(word) >= 3 and is_vowel(word[-3]):
            wordInflected = word + 'er'
        else:
            wordInflected = word + word[-1] + 'er'
    elif get_syllable_count(word) == 2 and is_vowel(word[-2]) and is_consonant(word[-1]) \
            and word[-1] != 'x' and word[-1] != 'w' and word[-1] != 'y':
        if is_final_syllable_stressed(word):
            wordInflected = word + word[-1] + 'er'
        else:
            wordInflected = word + 'er'
    else:
        wordInflected = word + "er"
    return wordInflected
