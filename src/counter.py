import src.inflection as infl

def remove_special_chars(text):
    special_chars = '+-*\\/"\'<>$&#@_}{][|¡!¿?:;,.='
    for char in special_chars:
        text = text.replace(char, ' ')
    return text

def regular_count(wordToFind, fileToAnalyze):
    count = 0

    fileToAnalyze.seek(0)
    textInFile = fileToAnalyze.read()

    # Removing the special characters from the text allows us to analyze files with formats like .html
    textInFile = remove_special_chars(textInFile) 
    wordsInText = textInFile.split()

    for word in wordsInText:
        if(word.lower() == wordToFind.lower()):
            count = count + 1

    return count

def inflection_count(wordToFind, fileToAnalyze):
    count = 0

    count += regular_count(wordToFind, fileToAnalyze)
    count += regular_count(infl.inflect_ing(wordToFind), fileToAnalyze)
    count += regular_count(infl.inflect_plural(wordToFind), fileToAnalyze)
    count += regular_count(infl.inflect_past(wordToFind), fileToAnalyze)
    count += regular_count(infl.inflect_er(wordToFind), fileToAnalyze)

    return count

def say_hello():
    print("Hello mmaguevo")