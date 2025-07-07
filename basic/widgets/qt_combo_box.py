from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QComboBox Widget')
        self.setFixedSize(QSize(400, 100))

        # === Widgets ===
        lb_dropdown = QLabel()
        lb_dropdown.setText('Programming Language')

        dropdown = QComboBox()
        dropdown_items = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
        dropdown_items.sort()
        dropdown.addItems(dropdown_items)
        dropdown.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        dropdown.setEditable(True)
        dropdown.setMaxCount(10)

        lb_text = QLabel()
        lb_text.setText('Programming Language Selected: ')

        lb_text_selected = QLabel()
        lb_text_selected.setText(dropdown.currentText())

        lb_index = QLabel()
        lb_index.setText('Programming Language Selected (Index): ')

        self.lb_index_selected = QLabel()
        self.lb_index_selected.setText(str(dropdown.currentIndex()))

        # === Signals ===
        dropdown.currentTextChanged.connect(lb_text_selected.setText)
        dropdown.currentIndexChanged.connect(self.setIndex)

        # === layouts ===
        v_left_layout = QVBoxLayout()
        v_left_layout.addWidget(lb_dropdown)
        v_left_layout.addWidget(lb_text)
        v_left_layout.addWidget(lb_index)

        v_right_layout = QVBoxLayout()
        v_right_layout.addWidget(dropdown)
        v_right_layout.addWidget(lb_text_selected)
        v_right_layout.addWidget(self.lb_index_selected)

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_left_layout)
        h_layout.addLayout(v_right_layout)

        # container
        container = QWidget()
        container.setLayout(h_layout)

        # Set the central widget to the Main Window
        self.setCentralWidget(container)

    # === slots ===
    def setIndex(self, i : int):
        self.lb_index_selected.setText(str(i))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()