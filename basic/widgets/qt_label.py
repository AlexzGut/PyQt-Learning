from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Label Widget')
        self.setFixedSize(QSize(350, 500))

        # === Label Widgets ===
        self.label_tl = QLabel('Top-Left')
        self.label_tl.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.label_tr = QLabel('Top-Right')
        self.label_tr.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)

        self.label_bl = QLabel('Bottom-Left')
        self.label_bl.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft)

        self.label_br = QLabel('Bottom-Left')
        self.label_br.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)

        self.label_ct = QLabel('Center-Top')
        self.label_ct.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)

        self.label_cb = QLabel('Center-Bottom')
        self.label_cb.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        self.label_c = QLabel('Centered')
        self.label_c.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.label_cc = QLabel('Centered - One Flag')
        self.label_cc.setAlignment(Qt.AlignmentFlag.AlignCenter)



        # === Layout ===
        v_layout_l = QVBoxLayout()
        v_layout_r = QVBoxLayout()

        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout_l)
        h_layout.addLayout(v_layout_r)

        v_layout_l.addWidget(self.label_tl)
        v_layout_l.addWidget(self.label_tr)
        v_layout_l.addWidget(self.label_bl)
        v_layout_l.addWidget(self.label_br)
        v_layout_r.addWidget(self.label_ct)
        v_layout_r.addWidget(self.label_cb)
        v_layout_r.addWidget(self.label_c)
        v_layout_r.addWidget(self.label_cc)

        # Container
        container = QWidget()
        container.setLayout(h_layout)

        # Set the central widget of the main window
        self.setCentralWidget(container)



app = QApplication(sys.argv)
app.setStyleSheet('''
    QLabel {
        border: 1px solid #fff;
        font-size: 15px;
        width: 150px;
    }
''')

window = MainWindow()
window.show()

app.exec()
