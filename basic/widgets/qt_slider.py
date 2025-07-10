from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QSlider
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QSlider Widget')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        v_slider = QSlider(Qt.Orientation.Vertical) 
        v_slider.setRange(-10, 10)
        v_slider.setSingleStep(2)

        h_slider = QSlider(Qt.Orientation.Horizontal)
        # This two methods can be used to set the value/position of the slider (initial position 0 by default)
        h_slider.setSliderPosition(50)
        # h_slider.setValue(90)

        # === Signals ===
        v_slider.valueChanged.connect(self.value_changed)
        v_slider.sliderMoved.connect(self.slider_moved)
        v_slider.sliderPressed.connect(self.slider_pressed)
        v_slider.sliderReleased.connect(self.slider_released)

        # === Layout ===
        v_layout = QVBoxLayout()
        v_layout.addWidget(v_slider)
        v_layout.addWidget(h_slider)

        # container
        container = QWidget()
        container.setLayout(v_layout)

        # Set the central widget of the Main Window
        self.setCentralWidget(container)

    def value_changed(self, value):
        print(f'Slider value changed: {value}')

    def slider_moved(self, position):
        print(f'Slider position changed: {position}')

    def slider_pressed(self):
        print('PRESSED')

    def slider_released(self):
        print('RELEASED')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())