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
        self.ui.pushOpenInputFile.clicked.connect(self.onClickOpenInputFile)
        self.ui.pushRun.clicked.connect(self.onClickRun)
    
    def onClickOpenInputFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "File to analyze...", "", 
                                                        "Plain Text Files (*.txt);;All Files (*.*)")
        self.ui.lineInputFileName.setText(filename[0])

    def onClickRun(self):
        args = self.generateArgsFromUi()
        
        if args.input_filename == '':
            self.showErrorMessage("Please select a file to analyze.")
            return
        if args.wordlist[0] == '':
            self.showErrorMessage("Please enter a valid word to search.")
            return

        self.ui.textResults.clear() # We clear the text edit before logging the current analysis
        logger = QtPlainTextLogger(self.ui.textResults)

        try:
            analysis.analyze(args, logger)
        except FileNotFoundError as e:
            self.showErrorMessage("File" + e.filename + "not found. Please enter valid filenames.")

    def showErrorMessage(self, message, title="Error"):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.show()

    # This empty class is used to mock the args class we need to pass to the CLI method that performs the analysis
    class Arguments():
        pass

    def generateArgsFromUi(self):
        args = self.Arguments()
        args.input_filename = self.ui.lineInputFileName.text()

        args.wordlist = [self.ui.lineWordToFind.text().strip()]

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