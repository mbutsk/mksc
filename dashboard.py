import json
import time
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
import config
from typing import *
import os

import utils


# keyboard

winkey = 'Win' if os.name == 'nt' else 'Meta'

kb_size = [448,183]
s = [27,27] # default key size

key_names = {
    1:  'Esc',
    2:  '1',
    3:  '2',
    4:  '3',
    5:  '4',
    6:  '5',
    7:  '6',
    8:  '7',
    9:  '8',
    10: '9',
    11: '0',
    12: '-',
    13: '=',
    14: 'Backspace',
    15: 'Tab',
    16: 'Q',
    17: 'W',
    18: 'E',
    19: 'R',
    20: 'T',
    21: 'Y',
    22: 'U',
    23: 'I',
    24: 'O',
    25: 'P',
    26: '[',
    27: ']',
    28: 'Enter',
    29: 'Ctrl',
    30: 'A',
    31: 'S',
    32: 'D',
    33: 'F',
    34: 'G',
    35: 'H',
    36: 'J',
    37: 'K',
    38: 'L',
    39: ';',
    40: '\'',
    41: '`',
    42: 'Left Shift',
    43: '\\',
    44: 'Z',
    45: 'X',
    46: 'C',
    47: 'V',
    48: 'B',
    49: 'N',
    50: 'M',
    51: ',',
    52: '.',
    53: '/',
    54: 'Right Shift',
    55: 'Print Screen',
    56: 'Alt',
    57: 'Space',
    58: 'Caps',
    59: 'F1',
    60: 'F2',
    61: 'F3',
    62: 'F4',
    63: 'F5',
    64: 'F6',
    65: 'F7',
    66: 'F8',
    67: 'F9',
    68: 'F10',
    69: 'Num Lock',
    70: 'Scroll Lock',
    71: 'Home',
    72: 'Up',
    73: 'Page Up',
    74: '- (Minus)',
    75: 'Left',
    76: 'Center',
    77: 'Right',
    78: '+ (Plus)',
    79: 'End',
    80: 'Down',
    81: 'Page Down',
    82: 'Insert',
    83: 'Delete',

    87: 'F11',
    88: 'F12',
    91: 'Windows/Super/Meta',
    93: 'Menu',
}

rects = {
    1:  ['Esc', 0,  0,*s],
    59: ['F1',  60, 0,*s],
    60: ['F2',  90, 0,*s],
    61: ['F3',  120,0,*s],
    62: ['F4',  150,0,*s],
    63: ['F5',  195,0,*s],
    64: ['F6',  225,0,*s],
    65: ['F7',  255,0,*s],
    66: ['F8',  285,0,*s],
    67: ['F9',  330,0,*s],
    68: ['F10', 360,0,*s],
    87: ['F11', 390,0,*s],
    88: ['F12', 420,0,*s],
    
    41: ['`', 0,  35,*s],
    2:  ['1', 30, 35,*s],
    3:  ['2', 60, 35,*s],
    4:  ['3', 90, 35,*s],
    5:  ['4', 120,35,*s],
    6:  ['5', 150,35,*s],
    7:  ['6', 180,35,*s],
    8:  ['7', 210,35,*s],
    9:  ['8', 240,35,*s],
    10: ['9', 270,35,*s],
    11: ['0', 300,35,*s],
    12: ['-', 330,35,*s],
    13: ['=', 360,35,*s],
    14: ['Backspace', 390,35,57,27],
    
    15: ['Tab', 0,  65,37,27],
    16: ['Q',   40, 65,*s],
    17: ['W',   70, 65,*s],
    18: ['E',   100,65,*s],
    19: ['R',   130,65,*s],
    20: ['T',   160,65,*s],
    21: ['Y',   190,65,*s],
    22: ['U',   220,65,*s],
    23: ['I',   250,65,*s],
    24: ['O',   280,65,*s],
    25: ['P',   310,65,*s],
    26: ['[',   340,65,*s],
    27: [']',   370,65,*s],
    43: ['\\',  400,65,47,27],
    
    58: ['Сaps', 0,  95,47,27],
    30: ['A',    50, 95,*s],
    31: ['S',    80, 95,*s],
    32: ['D',    110,95,*s],
    33: ['F',    140,95,*s],
    34: ['G',    170,95,*s],
    35: ['H',    200,95,*s],
    36: ['J',    230,95,*s],
    37: ['K',    260,95,*s],
    38: ['L',    290,95,*s],
    39: [';',    320,95,*s],
    40: ['\'',   350,95,*s],
    28: ['Enter',380,95,67,27],
    
    42: ['LShift',0,  125,57,27],
    44: ['Z',     60, 125,*s],
    45: ['X',     90, 125,*s],
    46: ['C',     120,125,*s],
    47: ['V',     150,125,*s],
    48: ['B',     180,125,*s],
    49: ['N',     210,125,*s],
    50: ['M',     240,125,*s],
    51: [',',     270,125,*s],
    52: ['.',     300,125,*s],
    53: ['/',     330,125,*s],
    54: ['RShift',360,125,87,27],
    
    29: ['Ctrl', 0,  155,32,27],
    91: [winkey, 35, 155,32,27],
    56: ['Alt',  70, 155,32,27],
    57: ['Space',105,155,202,27],
    93: ['Menu', 310,155,32,27],
    
    75: ['<',  345,155,32,27],
    72: [None, 380,155,32,12],
    80: [None, 380,170,32,12],
    77: ['>',  415,155,32,27],
}

# key stats as list

class KeyList(QScrollArea):
    def __init__(self, data:Dict[int,int]):
        '''
        Keystroke data as a scrollable list.
        '''
        super().__init__(None)
        self.setWindowTitle('Keystroke List')
        self.setFrameStyle(QFrame.NoFrame)

        self.setWidgetResizable(True)

        self.kc = True
        self.ad = True
        self.editing = False

        # sorting key controls
        self.kc_combo = QComboBox()
        self.kc_combo.addItems(['By scancode', 'By amount'])
        self.kc_combo.setCurrentIndex(int(self.kc))
        self.kc_combo.currentIndexChanged.connect(self.kc_change)

        # ascending/descending controls
        self.ad_combo = QComboBox()
        self.ad_combo.addItems(['Ascending', 'Descending'])
        self.ad_combo.setCurrentIndex(int(self.ad))
        self.ad_combo.currentIndexChanged.connect(self.ad_change)

        # adding elements
        self.data = data
        self.reload_data(data)


    def ad_change(self, index:int):
        '''
        Callback for changing Ascending/Descending sorting mode.
        '''
        if self.editing: return
        self.editing = True
        
        self.ad = index == 1
        self.reload_data()


    def kc_change(self, index:int):
        '''
        Callback for changing sorting mode.
        '''
        if self.editing: return
        self.editing = True

        self.kc = index == 1
        self.reload_data()


    def reload_data(self, data:Dict[int,int] = None):
        '''
        Reloads the data.
        '''
        if data == None:
            data = self.data

        layout = QVBoxLayout()

        # controls
        c_layout = QHBoxLayout()
        c_layout.addWidget(self.kc_combo)
        c_layout.addWidget(self.ad_combo)

        layout.addLayout(c_layout)

        # controls separator
        frame = QFrame()
        frame.setFrameStyle(QFrame.HLine | QFrame.Raised)
        frame.setLineWidth(1)
        layout.addWidget(frame)

        # sorting elements
        if not self.kc:
            data = dict(sorted(data.items(), reverse=self.ad))
        else:
            data = dict(sorted(data.items(), key=lambda x: x[1], reverse=self.ad))

        # adding elements
        for scancode, amount in data.items():
            row = QHBoxLayout()

            # title
            if scancode in key_names:
                name = key_names[scancode]
                title = QLabel(f"{name} ({scancode})")
            
            else:
                title = QLabel(f"Unknown scancode ({scancode})")
                title.setStyleSheet('color: gray')

            # amount
            amount_label = QLabel(f'{amount}')
            font = amount_label.font()
            font.setBold(True)
            amount_label.setFont(font)

            amount_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

            # adding widgets
            row.addWidget(title)
            row.addWidget(amount_label)

            layout.addLayout(row)

        # setting layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setMinimumWidth(widget.sizeHint().width()+30)
        self.setWidget(widget)

        self.editing = False


# window

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

        # keyboard layout
        self.kb_label = QLabel()
        self.kb_label.setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.kb_label)

        # full stats button
        button = QPushButton("View as list...")
        button.clicked.connect(self.show_keylist)
        layout.addWidget(button)

        self.kb_window = None

        # adding widgets
        layout.setAlignment(Qt.AlignTop)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        # reloading data
        self.kb_data = None
        self.reload()


    def show_keylist(self):
        if self.kb_data == None: return

        if self.kb_window == None:
            self.kb_window = KeyList(self.kb_data)
        self.kb_window.show()


    def redraw_keyboard(self, data:Dict[int,int]):
        '''
        Redraws the keyboard widget.
        '''
        print('Redrawing')

        # calculating data
        if len(data) != 0:
            max_val = max(data.values())
            percents = {
                k: v/max_val for k,v in data.items()
            }
        else:
            percents = {}

        # drawing keyboard
        canvas = QPixmap(*kb_size)
        canvas.fill(Qt.transparent)
        self.kb_label.setPixmap(canvas)

        painter = QPainter(self.kb_label.pixmap())

        for scancode, rect in rects.items():
            name = rect[0]
            rect = rect[1:]
            size = rect[2:]

            # color
            if scancode in data:
                amount = utils.shorten(data[scancode], 1)
                color = utils.get_heatmap_color(percents[scancode])
            else:
                amount = '0'
                color = '#%02x%02x%02x' % config.HEATMAP_COLORS[0]

            # rect
            brush = QBrush()
            brush.setStyle(Qt.SolidPattern)
            brush.setColor(QColor(color))
            painter.setBrush(brush)

            painter.drawRect(*rect)

            # amount
            font = QFont()
            font.setPointSize(6)
            painter.setFont(font)

            offset = 6 if name != None else 0
            painter.drawText(
                rect[0]+1, rect[1]-offset, *size,
                Qt.AlignHCenter | Qt.AlignCenter, amount
            )

            # name
            if name != None:
                font = QFont()
                font.setPointSize(8)
                painter.setFont(font)

                painter.drawText(
                    rect[0]+1, rect[1]+5, *size,
                    Qt.AlignHCenter | Qt.AlignCenter, name
                )
        
        painter.end()


    def keyPressEvent(self, event):
        '''
        Reloading upon pressing a key
        '''
        if isinstance(event, QKeyEvent):
            if event.key() == Qt.Key_F5:
                self.reload()


    def reload(self):
        '''
        Reloads data from a file.
        '''
        print("Reloading")

        try:
            with open(config.INDEX_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # mouse movements
            px = data['mouse_move']
            meters = px/config.PPM

            self.mouse_pixels.setText(f'{utils.shorten(px)}')
            self.mouse_meters.setText(utils.shorten_dist(meters))

            # keypresses
            values = data['keystrokes'].values()
            total = sum(values)

            self.kb_press.setText(f'{utils.shorten(total)}')

            # keyboard layout
            self.kb_data: Dict[int,int] = {
                int(k):v for k,v in data['keystrokes'].items()
            }
            self.redraw_keyboard(self.kb_data)

            # reloading menu
            if self.kb_window != None:
                self.kb_window.reload_data(self.kb_data)

        except Exception as e:
            print(f'Error reading file: {e}')

            self.mouse_pixels.setText('Error')
            self.mouse_meters.setText('Error')
            self.kb_press.setText('Error')


app = QApplication([])

window = Window()
window.show()

app.exec()
