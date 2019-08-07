import src.inflection as infl


def remove_special_chars(text):
    special_chars = '+-*\\/"\'<>$&#@_}{][|¡!¿?:;,.='
    for char in special_chars:
        text = text.replace(char, ' ')
    return text


def regular_count(word_to_find, file_to_analyze):
    count = 0

    file_to_analyze.seek(0)
    textInFile = file_to_analyze.read()

    # Removing the special characters from the text allows us to analyze files with formats like .html
    textInFile = remove_special_chars(textInFile)
    wordsInText = textInFile.split()

    for word in wordsInText:
        if(word.lower() == word_to_find.lower()):
            count = count + 1

    return count


def multiple_files_count(word_to_find, input_files_list):
    count = 0

    for file_to_analyze in input_files_list:
        file_to_analyze.seek(0)
        textInFile = file_to_analyze.read()

        # Removing the special characters from the text allows us to analyze files with formats like .html
        textInFile = remove_special_chars(textInFile)
        wordsInText = textInFile.split()

        for word in wordsInText:
            if(word.lower() == word_to_find.lower()):
                count = count + 1

    return count


def inflection_count(word_to_find, file_to_analyze):
    count = 0

    count += regular_count(word_to_find, file_to_analyze)
    count += regular_count(infl.inflect_ing(word_to_find), file_to_analyze)
    count += regular_count(infl.inflect_plural(word_to_find), file_to_analyze)
    count += regular_count(infl.inflect_past(word_to_find), file_to_analyze)
    count += regular_count(infl.inflect_er(word_to_find), file_to_analyze)

    return count