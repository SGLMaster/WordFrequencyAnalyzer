class CliLogger:
    def log(self, string):
        print(string)


class PlainTextFileLogger:
    def __init__(self, file):
        self.file = file

    def log(self, string):
        self.file.write(string + '\n')

    def close(self):
        self.file.close()


class QtPlainTextLogger:
    def __init__(self, textEdit):
        self.textEdit = textEdit

    def log(self, string):
        self.textEdit.appendPlainText(string)


class StrLogger:
    def __init__(self):
        self.string = ""

    def log(self, string):
        self.string += string + '\n'

    def get_string(self):
        return self.string


class TreeViewLogger:
    def log(self, string):
        pass
