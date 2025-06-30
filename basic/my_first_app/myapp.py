from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My First App')
        self.setFixedSize(QSize(400, 300))

        # === Widgets ===
        button = QPushButton('Submit')
        button.setFixedSize(QSize(100,100))

        # Set the central widget of the window
        self.setCentralWidget(button)


# One and only one instance of QApplication is needed per application.
# Command line arguments can be pass to the app using sys.argv, else
# QApplication([]) will do.
app =  QApplication(sys.argv)

# The window will be a Qt widget
# window = QWidget()
# window = QPushButton('Push me') # a window with a single push-able button in it
window = MainWindow()
window.show() # Windows are hidden by default, it's IMPORTANT to show it

# Start the event loop
app.exec()

# Once the event loop has been exited the application will reach this part
