# Import necessary modules
import sys
from PySide2.QtWidgets import(QApplication, QWidget, QPushButton,
                              QLabel, QButtonGroup, QHBoxLayout,
                              QVBoxLayout, QCheckBox)
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont


class Survey(QWidget):
    # constructor
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        # Initialize the window and display its contents to the screen

        self.setGeometry(1500, 200, 400, 300)
        self.setWindowTitle('survey')
        self.setAttribute(Qt.WA_ShowWithoutActivating)
        self.display_widgets()
        self.show()

    def display_widgets(self):
        # Set up widgets using QHBoxLayout and QVBoxLayout
        title = QLabel('Restaurent Survey', self)
        title.setFont(QFont('Arial', 20))

        question = QLabel('How would you rate our service?', self)
        question.move(25, 50)

        title_h_box = QHBoxLayout()
        title_h_box.addStretch()
        title_h_box.addWidget(title)
        title_h_box.addStretch()

        ratings = ['Not Satisfied', 'Average', 'Satisfied']

        ''' Create checkboxes and add them to horizontal layout, and add stretchable
        space on both sides of the widgets'''

        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(60)
        cb_h_box.addStretch()
        # Create button group to contain checkboxes
        scale_bg = QButtonGroup(self)

        for i in ratings:
            scale_cb = QCheckBox(i, self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()
        # Check for signal when checkbox is clicked
        scale_bg.buttonClicked.connect(self.check_box_clicked)

        close_btn = QPushButton('close', self)
        close_btn.clicked.connect(self.close)

        # Create vertical layout and add widgets and h_box layouts
        v_box = QVBoxLayout(self)
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(3)
        v_box.addWidget(close_btn)
        # Set main layout of the window
        self.setLayout(v_box)

    def check_box_clicked(self, cb):
        # Print the text of checkbox selected.
        print(cb.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Survey()
    sys.exit(app.exec_())

