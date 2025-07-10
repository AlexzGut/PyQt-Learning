from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QSpinBox, QDoubleSpinBox, QVBoxLayout, QWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QSpinBox Widget')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        spin_box = QSpinBox()
        # spin_box.setMinimum(-10)
        # spin_box.setMaximum(10)
        spin_box.setRange(-10, 10)
        spin_box.setPrefix('$')
        spin_box.setSuffix('c')

        d_spin_box = QDoubleSpinBox()
        # d_spin_box.setMinimum(-10)
        # d_spin_box.setMaximum(10)
        d_spin_box.setRange(-10, 10)
        d_spin_box.setPrefix('$')
        d_spin_box.setSuffix('c')
        d_spin_box.setSingleStep(0.1)

        # === Signals ===
        spin_box.valueChanged.connect(self.value_changed)
        spin_box.textChanged.connect(self.text_changed)

        d_spin_box.valueChanged.connect(self.d_value_changed)
        d_spin_box.textChanged.connect(self.d_text_changed)

        # === Layouts ===
        v_layout = QVBoxLayout()
        v_layout.addWidget(spin_box)
        v_layout.addWidget(d_spin_box)

        # container
        container = QWidget()
        container.setLayout(v_layout)
        
        # Set the central widget of the Main Window
        self.setCentralWidget(container)

    # === Slots ===
    def value_changed(self, v : int):
        print(f'QSpinBox value changed: {v}')

    def d_value_changed(self, v : int):
        print(f'QDoubleSpinBox value changed: {v}')

    def text_changed(self, v : str):
        print(f'QSpinBox text changed: {v}')
    
    def d_text_changed(self, v : str):
        print(f'QDoubleSpinBox text changed: {v}')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())