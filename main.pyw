from PyQt5 import QtWidgets, QtCore

from main_ui import Ui_MainWindow
from about_ui import Ui_DialogAbout

import src.analysis as analysis
from src.log import StrLogger

import traceback
import sys


class WorkerSignals(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    error = QtCore.pyqtSignal(tuple)
    result = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(dict, object)


class AnalysisWorker(QtCore.QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(AnalysisWorker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class DialogAbout(QtWidgets.QDialog, Ui_DialogAbout):
    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)

        self.dialog_ui = Ui_DialogAbout()
        self.dialog_ui.setupUi(self)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect events
        self.ui.pushOpenInputFile.clicked.connect(self.open_input_files)
        self.ui.pushRun.clicked.connect(self.create_analysis_thread)
        self.ui.pushAddWord.clicked.connect(self.add_word)
        self.ui.pushRemoveWord.clicked.connect(self.remove_word)
        self.ui.pushLoadWordsFromFile.clicked.connect(
            self.load_words_from_file)
        self.ui.lineWordToFind.returnPressed.connect(self.add_word)
        self.ui.pushSaveAs.clicked.connect(self.save_results)

        self.ui.actionAbout.triggered.connect(self.show_about_dialog)

        self.dialog_about = DialogAbout()

        self.threadpool = QtCore.QThreadPool()

    def open_input_files(self):
        self.input_filenames = QtWidgets.QFileDialog.getOpenFileNames(
            self, "File to analyze...", "", 
            "Plain Text Files (*.txt);;PDF (*.pdf);;HTML (*.html);;"
            + "All Files (*.*)")

        filenames_str = ""
        for filename in self.input_filenames[0]:
            filenames_str += filename + '; '

        self.ui.lineInputFileName.setText(filenames_str)

    def create_analysis_thread(self):
        self.args = self.generate_args_from_ui()

        if self.args.input_filename == '':
            self.show_error_message("Please select a file to analyze.")
            return
        if len(self.args.wordlist) == 0:
            self.show_error_message(
                "Please enter at least one word to search.")
            return

        self.ui.treeResults.clear()

        worker = AnalysisWorker(self.run_analysis)
        worker.signals.finished.connect(self.analysis_finished_callback)
        worker.signals.progress.connect(self.analysis_progress_callback)

        self.threadpool.start(worker)

    def run_analysis(self, progress_callback):
        filenames = []

        for i in range(len(self.input_filenames[0])):
            cur_filename = self.input_filenames[0][i]
            filenames.append(cur_filename)

        self.analyze_multiple_files(filenames, progress_callback)

    def analyze_multiple_files(self, filenames, progress_callback):
        word_list = self.args.wordlist
        number_of_words = len(word_list)

        progress_values = {"cur_word_number": 0,
                           "number_of_words": number_of_words}

        for i in range(number_of_words):
            cur_word = word_list[i]
            word_count = analysis.process_word(cur_word, self.args, filenames)

            progress_values["cur_word_number"] = i + 1
            progress_callback.emit(progress_values, word_count)

    def analysis_finished_callback(self):
        self.ui.progressBar.setValue(100)
        self.ui.labelProgress.setText("Finished")

    def analysis_progress_callback(self, progress_values, word_count):
        cur_word_number = progress_values["cur_word_number"]
        number_of_words = progress_values["number_of_words"]
        progress_percentage = (cur_word_number*100)//number_of_words

        self.ui.labelProgress.setText(
            "Processed " + str(cur_word_number) + "/" + str(number_of_words) 
            + " words")
        self.ui.progressBar.setValue(progress_percentage)

        self.fill_results_tree(word_count)

    def fill_results_tree(self, word_count):
        word_item = QtWidgets.QTreeWidgetItem(
            [word_count.get_word(),  str(word_count.get_total_count())])
        word_item.addChild(QtWidgets.QTreeWidgetItem(
            [word_count.get_word(),  str(word_count.get_normal_count())]))

        if self.args.switch_ing:
            word_item.addChild(QtWidgets.QTreeWidgetItem(
                [word_count.get_word_ing(),  
                str(word_count.get_ing_count())]))
        if self.args.switch_plural:
            word_item.addChild(QtWidgets.QTreeWidgetItem(
                [word_count.get_word_plural(),  
                str(word_count.get_plural_count())]))
        if self.args.switch_past:
            word_item.addChild(QtWidgets.QTreeWidgetItem(
                [word_count.get_word_past(),  
                str(word_count.get_past_count())]))
        if self.args.switch_er:
            word_item.addChild(QtWidgets.QTreeWidgetItem(
                [word_count.get_word_er(),  str(word_count.get_er_count())]))

        self.ui.treeResults.addTopLevelItem(word_item)

    def add_word(self):
        word = self.ui.lineWordToFind.text().strip()

        if word == '':
            self.show_information_message("Can't add empty word to list.")
            return

        wordlist = [str(self.ui.listWords.item(i).text().lower())
                    for i in range(self.ui.listWords.count())]
        if word.lower() in wordlist:
            self.show_information_message(
                "Word '" + word + "' is already in the list.")
            return

        self.ui.listWords.addItem(word)
        self.ui.listWords.sortItems()
        self.ui.lineWordToFind.clear()

    def remove_word(self):
        listWords = self.ui.listWords.selectedItems()
        if not listWords:
            return
        for word in listWords:
            self.ui.listWords.takeItem(self.ui.listWords.row(word))

    def load_words_from_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, "Load words...", "", "Plain Text Files (*.txt)")[0]
        try:
            words_file = open(filename, 'r')
            file_text = words_file.read()
            word_list = file_text.split()

            self.ui.listWords.addItems(word_list)
            self.ui.listWords.sortItems()

            words_file.close()

        except FileNotFoundError as e:
            self.show_error_message(
                "File " + e.filename 
                + " not found. Please enter a valid filename.")

    def save_results(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, "Save results...", "", "Plain Text Files (*.txt)")[0]

        try:
            fileToWrite = open(filename, 'w')
            results = self.ui.textResults.toPlainText()
            fileToWrite.write(results)
            fileToWrite.close
        except FileNotFoundError:
            pass

    def show_about_dialog(self):
        self.dialog_about.show()

    def show_error_message(self, message, title="Error"):
        self.show_message_common(
            message, title, QtWidgets.QMessageBox.Critical)

    def show_information_message(self, message, title="Info"):
        self.show_message_common(
            message, title, QtWidgets.QMessageBox.Information)

    def show_message_common(self, message, title, icon_type):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(icon_type)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.show()

    # This empty class is used to mock the args class we need to pass to
    # the CLI method that performs the analysis
    class Arguments():
        pass

    def generate_args_from_ui(self):
        args = self.Arguments()
        args.input_filename = self.ui.lineInputFileName.text()

        args.wordlist = [str(self.ui.listWords.item(i).text())
                         for i in range(self.ui.listWords.count())]

        args.switch_ing = self.ui.checkIng.isChecked()
        args.switch_plural = self.ui.checkPlural.isChecked()
        args.switch_past = self.ui.checkPast.isChecked()
        args.switch_er = self.ui.checkEr.isChecked()

        return args


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
