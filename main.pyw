from PyQt5 import QtWidgets

from main_ui import Ui_MainWindow

import src.cli as cli

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect events
        self.ui.pushOpenInputFile.clicked.connect(self.onClickOpenInputFile)
        self.ui.pushOpenOutputFile.clicked.connect(self.onClickOpenOutputFile)
        self.ui.pushRun.clicked.connect(self.onClickRun)
    
    def onClickOpenInputFile(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, "File to analyze...", "", 
                                                        "Plain Text Files (*.txt);;All Files (*.*)")
        self.ui.lineInputFileName.setText(filename[0])

    def onClickOpenOutputFile(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(self, "File to save results...", "Results", 
                                                        "Plain Text Files (*.txt)")
        self.ui.lineOutputFileName.setText(filename[0])

    def onClickRun(self):
        args = self.generateArgs()

        if args.wordlist[0] == '':
            self.showErrorMessage("Please enter a valid word to search.")
            return

        try:
            cli.analyze(args)
        except FileNotFoundError:
            self.showErrorMessage("File not found. Please enter valid filenames.")

    def showErrorMessage(self, message, title="Error"):
        msg = QtWidgets.QMessageBox(self)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.show()

    # This empty class is used to mock the args class we need to pass to the CLI method that performs the analysis
    class Arguments():
        pass

    def generateArgs(self):
        args = self.Arguments()
        args.input_filename = self.ui.lineInputFileName.text()
        args.output_filename = self.ui.lineOutputFileName.text()

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