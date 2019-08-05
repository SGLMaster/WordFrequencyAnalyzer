class CliLogger:
    def log(self, string):
        print(string)

class QtPlainTextLogger:
    def __init__(self, textEdit):
        self.textEdit = textEdit

    def log(self, string):
        self.textEdit.appendPlainText(string)