from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('CheckBox Widget')

        # === Widgets ===
        check_box = QCheckBox('One checkbox')
        check_box.setCheckState(Qt.CheckState.Checked)
        check_box.setTristate(True)

        self.label = QLabel('Checked')

        # === Signal ===
        check_box.stateChanged.connect(self.display_state)

        # layout
        v_layout = QVBoxLayout()
        v_layout.addWidget(check_box)
        v_layout.addWidget(self.label)

        # container
        container = QWidget()
        container.setLayout(v_layout)

        # Set the central widget of the main window
        self.setCentralWidget(container)

    # === slot ===
    def display_state(self, s):
        # state = 'Checked' if Qt.CheckState(s) == Qt.CheckState.Checked else 'Unchecked'
        state = {0 : 'Unchecked',
                 1 : 'Partially Checked',
                 2 : 'Checked'}
        self.label.setText(state.get(s))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


