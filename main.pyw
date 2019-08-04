from PyQt5 import QtWidgets

from main_ui import Ui_MainWindow

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
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()