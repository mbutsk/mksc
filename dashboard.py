import json
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
import config
from typing import *

import utils


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MKSC Dashboard")

        # creating page layout
        layout = QVBoxLayout()

        # F5 label
        title_layout = QHBoxLayout()

        title = QLabel("MKSC")
        font = title.font()
        font.setBold(True)
        font.setPointSize(18)
        title.setFont(font)
        title_layout.addWidget(title)

        f5 = QLabel("Press F5 to reload")
        f5.setStyleSheet('color: gray')
        title_layout.addWidget(f5)
        f5.setAlignment(Qt.AlignRight | Qt.AlignCenter)

        layout.addLayout(title_layout)
        
        # mouse stats splitter
        frame = QFrame()
        frame.setFrameStyle(QFrame.HLine | QFrame.Raised)
        frame.setLineWidth(2)
        layout.addWidget(frame)

        # mouse stats title
        title = QLabel("Mouse Move Stats")
        font = title.font()
        font.setBold(True)
        font.setPointSize(10)
        title.setFont(font)
        layout.addWidget(title)

        # stats
        self.mouse_pixels = QLabel("Loading...")
        self.mouse_pixels.setAlignment(Qt.AlignRight)

        self.mouse_meters = QLabel("Loading...")
        self.mouse_meters.setAlignment(Qt.AlignRight)

        pixels_layout = QHBoxLayout()

        label = QLabel("Pixels: ")
        label.setStyleSheet('color: gray')

        pixels_layout.addWidget(label)
        pixels_layout.addWidget(self.mouse_pixels)
        layout.addLayout(pixels_layout)

        label = QLabel("Distance: ")
        label.setStyleSheet('color: gray')

        meters_layout = QHBoxLayout()
        meters_layout.addWidget(label)
        meters_layout.addWidget(self.mouse_meters)
        layout.addLayout(meters_layout)
        
        # keyboard stats splitter
        frame = QFrame()
        frame.setFrameStyle(QFrame.HLine | QFrame.Raised)
        frame.setLineWidth(1)
        layout.addWidget(frame)

        # keyboard stats title
        title = QLabel("Keyboard Stats")
        font = title.font()
        font.setBold(True)
        font.setPointSize(10)
        title.setFont(font)
        layout.addWidget(title)

        # keyboard press stats
        kb_layout = QHBoxLayout()

        self.kb_press = QLabel("Loading...")
        self.kb_press.setAlignment(Qt.AlignRight)

        label = QLabel("Total keypresses: ")
        label.setStyleSheet('color: gray')

        kb_layout.addWidget(label)
        kb_layout.addWidget(self.kb_press)

        layout.addLayout(kb_layout)

        # adding widgets
        layout.setAlignment(Qt.AlignTop)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # reloading data
        self.reload()

    def reload(self):
        '''
        Reloads data from a file.
        '''
        try:
            with open(config.INDEX_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # mouse movements
            px = data['mouse_move']
            meters = px/config.PPM

            self.mouse_pixels.setText(f'{utils.shorten(px)}')
            self.mouse_meters.setText(utils.shorten_dist(meters))

            # keypresses
            total = sum(data['keystrokes'].values())

            self.kb_press.setText(f'{utils.shorten(total)}')

        except Exception as e:
            print(f'Error reading file: {e}')

            self.mouse_pixels.setText('Error')
            self.mouse_meters.setText('Error')


app = QApplication([])

window = Window()
window.show()

app.exec()
