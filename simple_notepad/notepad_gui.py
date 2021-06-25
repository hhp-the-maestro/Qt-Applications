import sys
from PySide2.QtWidgets import (QApplication, QWidget, QPushButton, QMessageBox,
                               QFileDialog, QTextEdit)
from PySide2.QtCore import Qt

class Notepad(QWidget):
    # Constructor
    def __init__(self):
        super().__init__()
        self.initialize_ui()  # initializing the UI function

    # create the main UI
    def initialize_ui(self):
        self.setGeometry(1500, 200, 400, 500)
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.setWindowTitle('notepad')
        self.display_widgets()  # calling the function which creates the notepads widget
        self.show()

    # Create widgets for notepad GUI and arrange them in window
    def display_widgets(self):
        # new file button
        new_button = QPushButton('New', self)
        new_button.move(20, 20)
        new_button.clicked.connect(self.clear_text)
        # save file button
        save_btn = QPushButton('Save', self)
        save_btn.move(120, 20)
        save_btn.clicked.connect(self.save_text)
        # the text field
        self.text_field = QTextEdit(self)
        self.text_field.setLineWrapMode(QTextEdit.LineWrapMode())
        self.text_field.move(10, 60)
        self.text_field.resize(380, 420)

    # If the new button is clicked , display dialog
    # asking user if they want to clear the text edit field
    # or not.
    def clear_text(self):
        ans = QMessageBox.question(self, 'clear text',
                                   'Do you want to clear text without saving',
                                   QMessageBox.No|QMessageBox.Yes, QMessageBox.Yes)
        if ans == QMessageBox.Yes:
            self.text_field.clear()
        else:
            pass

    """If the save button is clicked, display dialog
to save the text in the text edit field to a text
file."""
    def save_text(self):
        options = QFileDialog.Options()
        notepad_text = self.text_field.toPlainText()
        file_name = QFileDialog.getSaveFileName(self, 'Save File', "",
                                                "All Files (*);; Text Files (*.txt)",
                                                options=options)
        if file_name[0]:
            with open(file_name[0], 'w') as f:
                f.write(notepad_text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Notepad()
    sys.exit(app.exec_())


