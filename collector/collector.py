from copy import deepcopy
import os
import threading
import time
from typing import *
import win10toast
import json
import keyboard
import pyautogui
import utils


class Collector:
    def __init__(self, index_file: str):
        '''
        A collector class.
        '''
        keyboard.on_release(self.on_key_press)

        self.file: str = index_file

        self.toaster = win10toast.ToastNotifier()
        
        self.read()

        self.finished: bool = False
        self.changed: bool = False

        self.write_in: int = 12

        self.prev_pos = None
        self.mouse_pos = None


    def on_key_press(self, key):
        '''
        Logs keystrokes.
        '''
        key = key.scan_code

        # global stats
        if key not in self.keystrokes:
            self.keystrokes[key] = 0

        self.keystrokes[key] += 1

        self.changed = True
        

    def write(self):
        '''
        Rewrites the data to the index file.
        '''
        try:
            data = {
                "keystrokes": self.keystrokes,
                "mouse_move": self.mouse_move
            }

            with open(self.file, 'w', encoding='utf-8') as f:
                json.dump(data, f)

        except Exception as e:
            self.toaster.show_toast(
                "MKSC Error",
                f"Unable to write to index file: {e}\nAborting. Please relaunch the program",
                duration=5
            )
            self.finished = True


    def new(self):
        '''
        Creates a new file.
        '''
        self.keystrokes: Dict[int,int] = {}
        self.mouse_move: int = 0


    def read(self):
        '''
        Reads the stats from the file.
        '''
        if not os.path.exists(self.file):
            self.new()
            return

        # index
        try:
            with open(self.file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.keystrokes: Dict[int,int] = {
                int(k): v for k, v in data["keystrokes"].items()
            }
            self.mouse_move: int = data["mouse_move"]

        except Exception as e:
            self.toaster.show_toast(
                "MKSC Error",
                f"File cannot be read: {e}\nAborting. Please relaunch the program",
                duration=15
            )
            self.finished = True


    def loop(self, icon):
        '''
        A loop that logs the stats.
        '''
        while not self.finished:
            # getting mouse movements
            self.prev_pos = deepcopy(self.mouse_pos)
            self.mouse_pos = pyautogui.position()

            if self.prev_pos != None\
                and self.mouse_pos != self.prev_pos:
                    distance = utils.get_distance(self.mouse_pos, self.prev_pos)
                    self.mouse_move += int(distance)

                    self.changed = True

            # writing the data
            if self.write_in == 0:
                if self.changed:
                    self.write()
                    self.changed = False

                self.write_in = 20

            else:
                self.write_in -= 1

            # waiting
            time.sleep(0.1)

        # aborting if needed
        self.write()
        icon.stop()
        exit()


    def begin(self, icon):
        '''
        Starts the threaded loop.
        '''
        self.finished = False

        threading.Thread(target=self.loop, args=(icon,)).start()