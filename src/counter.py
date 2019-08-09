import io
 
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

import src.inflection as infl

def remove_special_chars(text):
    special_chars = '+-*\\/"\'<>$&#@_}{][|¡!¿?:;,.='
    for char in special_chars:
        text = text.replace(char, ' ')
    return text


def get_word_count(word_to_find, filenames):
    count = 0

    for cur_filename in filenames:
        if cur_filename.endswith(".pdf"):
            # PDF Miner
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
            with open(cur_filename, 'rb') as file_to_analyze:
                for page in PDFPage.get_pages(file_to_analyze, caching=True, check_extractable=True):
                    page_interpreter.process_page(page)
 
            text_in_file = fake_file_handle.getvalue()
 
            converter.close()
            fake_file_handle.close()
        else:
            with open(cur_filename, 'r', encoding="utf-8") as file_to_analyze:
                text_in_file = file_to_analyze.read()

        text_in_file = remove_special_chars(text_in_file)
        words_in_text = text_in_file.split()

        for word in words_in_text:
            if(word.lower() == word_to_find.lower()):
                count = count + 1

    return count