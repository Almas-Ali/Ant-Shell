from AntInterpreter import AntInterpreter
from TkTerm.tkterm import *
from Ant.src.lib.core import __version__ as version
from tkinter import messagebox

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

def on_closing():
    """ Exit dialog box """

    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Ant Shell")
    root.geometry("700x400")

    terminal = Terminal(root, text=SPLASH_ASCII, init=False)
    terminal.pack(fill=BOTH, expand=True)

    interpreter = AntInterpreter()
    terminal.add_interpreter("Ant", interpreter, set_default=True)

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
