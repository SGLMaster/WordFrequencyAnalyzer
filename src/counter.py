import src.inflection as infl

def regular_count(wordToFind, fileToAnalyze):
    count = 0

    fileToAnalyze.seek(0)
    textInFile = fileToAnalyze.read()

    wordsInText = textInFile.split()

    for word in wordsInText:
        if(word.lower().strip('-*\\/."\' ') == wordToFind.lower()):
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