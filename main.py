import tkinter as tk
from tkinter import *
from TkTerm.tkterm import Terminal

from AntInterpreter2 import AntInterpreter2
from Ant.src.lib.core import __version__ as version
import os

SPLASH_ASCII = f"""
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████
                                                                             
                                                                             
     █████  ███    ██ ████████     ███████ ██   ██ ███████ ██      ██        
    ██   ██ ████   ██    ██        ██      ██   ██ ██      ██      ██        
    ███████ ██ ██  ██    ██        ███████ ███████ █████   ██      ██        
    ██   ██ ██  ██ ██    ██             ██ ██   ██ ██      ██      ██        
    ██   ██ ██   ████    ██        ███████ ██   ██ ███████ ███████ ███████   
                                                                             
    ANT Interpreter version: {version}
    Powered by TkTerm
                                                                             
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████
"""

WARNING_ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "./warning.png"))

class RootWrapper():

    def __init__(self, master):

        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self._diaglog_box)

    def _diaglog_box(self):

        self.top = tk.Toplevel()
        self.top.title("Close this terminal?")
        self.top.resizable(False, False)

        width = 320
        height = 130

        # Set dialog box geometry
        self.top.geometry("{}x{}".format(width, height))

        # Get master current position
        root_x = self.master.winfo_x()
        root_y = self.master.winfo_y()

        # Get master width and height
        root_width = self.master.winfo_width()
        root_height = self.master.winfo_height()

        # Work out the new center coordinate
        x = root_x + (root_width/2) - (width/2)
        y = root_y + (root_height/2) - (height/2)

        # Position dialog box to center
        self.top.geometry("+%d+%d" % (x, y))

        # Make top a subwindow on root window
        self.top.transient(self.master)

        # Stop user interacting with other windows
        self.top.grab_set()

        ########################################################################
        ## Create dialog box
        ########################################################################

        self.frameWrap = tk.Frame(self.top, bg="#303030")
        self.frameWrap.pack(fill=BOTH, expand=True)

        frameBody = tk.Frame(self.frameWrap, bg="#303030")
        frameBody.pack(side=TOP, ipadx=20, ipady=20)

        frameButton = tk.Frame(self.frameWrap, bg="#303030", bd=0)
        frameButton.pack(side=BOTTOM, fill=X)

        buttonOptions = {
            "relief"                : FLAT,
            "bd"                    : 0,
            "height"                : 2,
            "highlightthickness"    : 0,
            "font"                  : ("Helvetica", 8)
        }

        buttonCancel = tk.Button(frameButton, text="Cancel", bg="#303030", fg="white", **buttonOptions , command=self._cancel)
        buttonCancel.pack(side=LEFT, pady=0, padx=0, fill=X, expand=True)

        buttonExit = tk.Button(frameButton, text="Exit Terminal", bg="orange", **buttonOptions , command=self._exit)
        buttonExit.pack(side=LEFT, pady=0, padx=0, fill=X, expand=True)

        # Fixes for Windows
        if os.name == "nt":
            buttonCancel.bind("<Enter>", lambda e: buttonCancel.config(fg="black", bg="#ececec"))
            buttonCancel.bind("<Leave>", lambda e: buttonCancel.config(fg="white", bg="#303030"))

            buttonExit.bind("<Enter>", lambda e: buttonExit.config(fg="black", bg="#ececec"))
            buttonExit.bind("<Leave>", lambda e: buttonExit.config(fg="black", bg="orange"))
        else:
            buttonCancel["activebackground"] = "#ececec"
            buttonCancel["activeforeground"] = "black"

            buttonExit["activebackground"] = "#ececec"
            buttonExit["activeforeground"] = "black"

        self.warningIcon = tk.PhotoImage(file=WARNING_ICON_PATH)
        icon = tk.Label(frameBody, image=self.warningIcon, bg="#303030")
        icon.pack(side=LEFT, padx=10)

        label = tk.Label(frameBody, text="Are you sure you want to exit the terminal?", bg="#303030", fg="white", font=("Helvetica", 8))
        label.pack(side=LEFT, padx=10)

        # Wait until top closes before return to root
        self.master.wait_window(self.top)

    def _exit(self):
        self.master.destroy()

    def _cancel(self):
        self.top.destroy()

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Ant Shell")
    root.geometry("700x400")

    terminal = Terminal(root, text=SPLASH_ASCII, init=False)
    terminal.pack(fill=BOTH, expand=True)

    icon = PhotoImage(file="ant.png")
    root.iconphoto(False, icon)

    interpreter = AntInterpreter2(gui_element=root)
    terminal.add_interpreter("Ant", interpreter, icon=icon, set_default=True)

    RootWrapper(root)
    root.mainloop()
