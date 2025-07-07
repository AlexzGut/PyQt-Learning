from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QListWidget widget')
        self.setFixedSize(QSize(400, 300))

        # === Widget ===
        self.list_w = QListWidget()
        self.list_w.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        items = ['Send Email',  'Download', 'Both']
        items.sort()
        self.list_w.addItems(items)

        # === Signals ===
        self.list_w.currentTextChanged.connect(self.text_changed)
        self.list_w.currentItemChanged.connect(self.item_changed)
        self.list_w.selectionModel().selectionChanged.connect(self.selection_changed)

        # Set the central widget of the main window
        self.setCentralWidget(self.list_w)

    # === Slots ===
    def text_changed(self, s : str):
        print(f'Item selected (text): {s}')

    def item_changed(self, i : QListWidgetItem):
        print(f'Item selected: {i}, text: {i.text()}')

    def selection_changed(self):
        items = []
        for i in self.list_w.selectedItems():
            items.append(i.text())
        print(f'Items selected: {items}')


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()