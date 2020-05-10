#UI

import tkinter as tk
from tkinter import ttk

class Home(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.FrameSwitch(Home)
    def FrameSwitch(self, frameClass):
        newFrame = frameClass(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = newFrame
        self._frame.pack()
