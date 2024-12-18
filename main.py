from gui import Interface
from statement import Statements
from tkinter import *
from file_processing import FileProcessor


class App:
    def __init__(self):
        self.window = Tk()
        self.file_handler = FileProcessor(self.window, "data/statements")
        self.statements = Statements().all_statements

    def start_app(self):
        ui = Interface(self.window,
                       self.statements,
                       self.upload_statement,
                       self.file_handler
                       )

        self.window.mainloop()

    def upload_statement(self, file_name):
        self.file_handler.upload_file(file_name)


if __name__ == "__main__":
    app = App()
    app.start_app()
