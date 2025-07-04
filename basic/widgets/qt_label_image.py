from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
import sys
import os

basedir = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Display image on QLabel')
        # self.setFixedSize(QSize(300, 400))

        # Pixmap
        pixmap = QPixmap(os.path.join(basedir, 'resources\\excel-icon.png'))

        # === Label ===
        self.label = QLabel()
        self.label.setPixmap(pixmap)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # self.label.setScaledContents(True)

        # Set the central widget of the main window
        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
app.setStyleSheet('''
    QLabel {
        border: 1px solid #fff;
        border-radius: 5px;
    }
''')

window = MainWindow()
window.show()

app.exec()
