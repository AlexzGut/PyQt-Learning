from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QDial
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QDial Widget')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        dial = QDial()
        dial.setRange(-100, 100)
        dial.setSliderPosition(30)

        # === Signals ===
        dial.valueChanged.connect(self.value_changed)
        dial.sliderMoved.connect(self.slider_moved)
        dial.sliderPressed.connect(self.slider_pressed)
        dial.sliderReleased.connect(self.slider_released)

        # === Layout ===
        v_layout = QVBoxLayout()
        v_layout.addWidget(dial)

        # container
        container = QWidget()
        container.setLayout(v_layout)

        # Set central widget of the Main Window
        self.setCentralWidget(container)

    # === Slots ===
    def value_changed(self, value):
        print(f'QDial value changed: {value}')

    def slider_moved(self, position):
        print(f'QDial position changed: {position}')

    def slider_pressed(self):
        print('PRESSED')

    def slider_released(self):
        print('RELEASED')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())