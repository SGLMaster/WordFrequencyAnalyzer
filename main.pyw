from PyQt5 import QtWidgets

from main_ui import Ui_MainWindow

import src.analysis as analysis
from src.log import QtPlainTextLogger

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect events
        self.ui.pushOpenInputFile.clicked.connect(self.open_input_file)
        self.ui.pushRun.clicked.connect(self.run_analysis)
        self.ui.pushAddWord.clicked.connect(self.add_word)
        self.ui.lineWordToFind.returnPressed.connect(self.add_word)
        self.ui.pushSaveAs.clicked.connect(self.save_results)
    
    def open_input_file(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "File to analyze...", "", 
                                                        "Plain Text Files (*.txt);;All Files (*.*)")[0]
        self.ui.lineInputFileName.setText(filename)

    def run_analysis(self):
        args = self.generate_args_from_ui()
        
        if args.input_filename == '':
            self.show_error_message("Please select a file to analyze.")
            return
        if args.wordlist[0] == '':
            self.show_error_message("Please enter a valid word to search.")
            return

        self.ui.textResults.clear() # We clear the text edit before logging the current analysis
        logger = QtPlainTextLogger(self.ui.textResults)

        try:
            analysis.analyze(args, logger)
        except FileNotFoundError as e:
            self.show_error_message("File" + e.filename + "not found. Please enter valid filenames.")

    def add_word(self):
        self.ui.listWords.addItem(self.ui.lineWordToFind.text())
        self.ui.lineWordToFind.clear()

    def save_results(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "File to analyze...", "", "Plain Text Files (*.txt)")[0]

        try:
            fileToWrite = open(filename, 'w')
            results = self.ui.textResults.toPlainText()
            fileToWrite.write(results)
            fileToWrite.close
        except FileNotFoundError:
            pass

    def show_error_message(self, message, title="Error"):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.show()

    # This empty class is used to mock the args class we need to pass to the CLI method that performs the analysis
    class Arguments():
        pass

    def generate_args_from_ui(self):
        args = self.Arguments()
        args.input_filename = self.ui.lineInputFileName.text()

        args.wordlist = [str(self.ui.listWords.item(i).text()) for i in range(self.ui.listWords.count())]

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