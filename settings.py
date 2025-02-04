
#importing necessary modules
from PySide6.QtWidgets import QDialog, QWidget, QPushButton, QStackedWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap



class Setting(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        icon = QPixmap("images/NoteBook.png").scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.setWindowIcon(icon)
        self.setGeometry(450, 250, 415, 200)
        self.setMinimumWidth(415)
        self.setMinimumHeight(150)
        self.stack = QStackedWidget(self)

        #making the main window
        main_window = QWidget(self)
        self.stack.addWidget(main_window)

        layout = QVBoxLayout()

        home_message = QLabel("This is Under Development So This will not be Everything after the Launch:", self)
        layout.addWidget(home_message)

        first_window_button = QPushButton("First window")
        first_window_button.clicked.connect(self.first_window_change)
        layout.addWidget(first_window_button)

        second_window_button = QPushButton("Second window")
        second_window_button.clicked.connect(self.second_window_change)
        layout.addWidget(second_window_button)

        third_window_button = QPushButton("Third window")
        third_window_button.clicked.connect(self.third_window_change)
        layout.addWidget(third_window_button)

        main_window.setLayout(layout)

        

        first_window = QWidget(self)
        self.stack.addWidget(first_window)
        home_window_button = QPushButton("home", self)
        home_window_button.clicked.connect(self.home_window_change)

        label_1 = QLabel("This is the first window right here: ", self)

        layout_1 = QVBoxLayout()
        layout_1.addWidget(home_window_button)
        layout_1.addWidget(label_1)
        first_window.setLayout(layout_1)





        second_window = QWidget(self)
        self.stack.addWidget(second_window)
        home_window_button_1 = QPushButton("home", self)
        home_window_button_1.clicked.connect(self.home_window_change)

        label_2 = QLabel("This is the Second Window right Here: ", self)

        layout_2 = QVBoxLayout()
        layout_2.addWidget(home_window_button_1)
        layout_2.addWidget(label_2)
        second_window.setLayout(layout_2)





        third_window = QWidget(self)
        self.stack.addWidget(third_window)
        home_window_button_2 = QPushButton("home", self)
        home_window_button_2.clicked.connect(self.home_window_change)

        label_3 = QLabel("This is the Third Window Right Here: ", self)

        layout_3 = QVBoxLayout()
        layout_3.addWidget(home_window_button_2)
        layout_3.addWidget(label_3)
        third_window.setLayout(layout_3)


    def first_window_change(self):
        self.stack.setCurrentIndex(1)
        self.setWindowTitle("first window")
    def second_window_change(self):
        self.stack.setCurrentIndex(2)
        self.setWindowTitle("second window")

    def third_window_change(self):
        self.stack.setCurrentIndex(3)
        self.setWindowTitle("third window")

    def home_window_change(self):
        self.stack.setCurrentIndex(0)
        self.setWindowTitle("Settings")
