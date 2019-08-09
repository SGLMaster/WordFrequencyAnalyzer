import io

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import src.inflection as infl


class WordCount:
    def __init__(self, word):
        self._word = word
        self._word_ing = infl.inflect_ing(word)
        self._word_plural = infl.inflect_plural(word)
        self._word_past = infl.inflect_past(word)
        self._word_er = infl.inflect_er(word)

        self._normal_count = 0
        self._ing_count = 0
        self._plural_count = 0
        self._past_count = 0
        self._er_count = 0
        self._total_count = 0

    def get_word(self): return self._word
    def get_word_ing(self): return self._word_ing
    def get_word_plural(self): return self._word_plural
    def get_word_past(self): return self._word_past
    def get_word_er(self): return self._word_er

    def get_normal_count(self): return self._normal_count

    def set_normal_count(self, count):
        self._normal_count = count
        self._calculate_total()

    def get_ing_count(self): return self._ing_count

    def set_ing_count(self, count):
        self._ing_count = count
        self._calculate_total()

    def get_plural_count(self): return self._plural_count

    def set_plural_count(self, count):
        self._plural_count = count
        self._calculate_total()

    def get_past_count(self): return self._past_count

    def set_past_count(self, count):
        self._past_count = count
        self._calculate_total()

    def get_er_count(self): return self._er_count

    def set_er_count(self, count):
        self._er_count = count
        self._calculate_total()

    def get_total_count(self): return self._total_count

    def _calculate_total(self):
        self._total_count = self._normal_count + self._ing_count \
        + self._plural_count + self._past_count + self._er_count


def remove_special_chars(text):
    special_chars = '+-*\\/"\'<>$&#@_}{][|¡!¿?:;,.='
    for char in special_chars:
        text = text.replace(char, ' ')
    return text


def get_word_count(word_to_find, filenames):
    count = 0

    for cur_filename in filenames:
        text_in_file = get_text_from_file(cur_filename)
        text_in_file = remove_special_chars(text_in_file)
        words_in_text = text_in_file.split()

        for word in words_in_text:
            if(word.lower() == word_to_find.lower()):
                count = count + 1

    return count

def get_text_from_file(filename):
    text_in_file = ""

    if filename.endswith(".pdf"):
        text_in_file = get_text_from_pdf(filename)
    else:
        with open(filename, 'r', encoding="utf-8") as file_to_analyze:
            text_in_file = file_to_analyze.read()

    return text_in_file

def get_text_from_pdf(filename):
    # PDF Miner
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    with open(filename, 'rb') as file_to_analyze:
        for page in PDFPage.get_pages(file_to_analyze, caching=True, 
        check_extractable=True):
            page_interpreter.process_page(page)

    text_in_file = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()

    return text_in_file