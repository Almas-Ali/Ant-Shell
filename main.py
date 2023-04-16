import tkinter as tk
from tkinter import *
from TkTerm.tkterm import Terminal, ExitDiaglogBox

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

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Ant Shell")
    root.geometry("700x400")

    terminal = Terminal(root, text=SPLASH_ASCII)
    terminal.pack(fill=BOTH, expand=True)

    icon = PhotoImage(file="ant.png")
    root.iconphoto(False, icon)

    interpreter = AntInterpreter2(gui_element=root)
    terminal.add_interpreter("Ant", interpreter, icon=icon, set_default=True)

    ExitDiaglogBox(root, icon=icon)
    root.mainloop()
