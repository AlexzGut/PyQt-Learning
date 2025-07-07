from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QComboBox Widget')
        self.setFixedSize(QSize(400, 100))

        # === Widgets ===
        lb_drop_down = QLabel()
        lb_drop_down.setText('Programming Language')

        drop_down = QComboBox()
        drop_down.addItems(['Python', 'Java', 'C++', 'JavaScript', 'Go'])

        lb = QLabel()
        lb.setText('Programming Language Selected: ')

        lb_selection = QLabel()
        lb_selection.setText(drop_down.currentText())

        # === Signals ===
        drop_down.currentTextChanged.connect(lb_selection.setText)

        # === layouts ===
        h_layout = QHBoxLayout()
        h_layout.addWidget(lb_drop_down)
        h_layout.addWidget(drop_down)

        h_selection_layout = QHBoxLayout()
        h_selection_layout.addWidget(lb)
        h_selection_layout.addWidget(lb_selection)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addLayout(h_selection_layout)

        # container
        container = QWidget()
        container.setLayout(v_layout)

        # Set the central widget to the Main Window
        self.setCentralWidget(container)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()