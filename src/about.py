from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QMargins, QRect, QPoint
import os
from settings import base_dir
import webbrowser


class AboutDlg(QDialog):
    name = "about"
    # Class functions(methods)
    def __init__(self, parent):
        super().__init__()
        # Setup the window
        self.setWindowTitle("About Sublimeless_ZK")
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # Setup the picture
        picture = QPixmap(os.path.join(base_dir(), 'app_picture.png'))

        self.picture = QLabel(self)
        self.picture.setPixmap(picture)
        self.picture.setGeometry(self.frameGeometry())
        self.picture.setScaledContents(False)
        # Assign events
        self.picture.mousePressEvent        = self._close
        self.picture.mouseDoubleClickEvent  = self._close
        # Initialize layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.picture)
        label1 = QLabel('Sublimeless_ZK')
        label2 = QLabel('(c) in 2018 by Rene Schallner')
        label3 = QPushButton('https://github.com/renerocksai')
        label1.setStyleSheet('font: 20px bold; color: yellow')
        label2.setStyleSheet('font: 16px bold; color: white')
        label3.setStyleSheet('font: 14px bold; background-color: lightgrey; color: #fd971f; margin: 2px')
        label3.setFlat(True)
        label3.setAutoFillBackground(False)
        label3.clicked.connect(self.url_clicked)
        vlay = QVBoxLayout()

        vlay.addWidget(label1, alignment=Qt.AlignHCenter)
        vlay.addWidget(label2, alignment=Qt.AlignHCenter)
        vlay.addWidget(label3, alignment=Qt.AlignHCenter)
        self.layout.addLayout(vlay, 0, 0, Qt.AlignCenter)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(QMargins(0 ,0 ,0 ,0))
        self.setLayout(self.layout)
        # Set the log window icon
        self.setWindowIcon(QIcon(os.path.join(base_dir(), 'app_logo_64.png')))
        my_width    = 512
        my_height   = 200
        # Set the info window position
        parent_left     = parent.geometry().left()
        parent_top      = parent.geometry().top()
        parent_width    = parent.geometry().width()
        parent_height   = parent.geometry().height()
        my_left = parent_left + (parent_width/2) - (my_width/2)
        my_top = parent_top + (parent_height/2) - (my_height/2)
        self.setGeometry(QRect(my_left, my_top, my_width, my_height))
        self.setFixedSize(my_width, my_height)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.Dialog | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)




    def _close(self, event):
        """Close the widget"""
        self.picture.setParent(None)
        self.picture = None
        self.layout = None
        self.close()

    def url_clicked(self):
        webbrowser.open('https://github.com/renerocksai/')
        self.close()