from AntInterpreter import AntInterpreter
from TkTerm.tkterm import *
from Ant.src.lib.core import __version__ as version


SPLASH_ASCII = f"""
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 
                                                                              
                                                                              
     █████  ███    ██ ████████     ███████ ██   ██ ███████ ██      ██         
    ██   ██ ████   ██    ██        ██      ██   ██ ██      ██      ██         
    ███████ ██ ██  ██    ██        ███████ ███████ █████   ██      ██         
    ██   ██ ██  ██ ██    ██             ██ ██   ██ ██      ██      ██         
    ██   ██ ██   ████    ██        ███████ ██   ██ ███████ ███████ ███████    
                                                                              
                                                                              
    Version: {version}
                                                                              
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 
                                                                              
"""


root = tk.Tk()
root.title("Ant Shell")
root.geometry("700x400")

terminal = Terminal(root, text=SPLASH_ASCII)
terminal.pack(fill=BOTH, expand=True)

interpreter = AntInterpreter()
terminal.add_interpreter("Ant", interpreter, set_default=True)

root.mainloop()
