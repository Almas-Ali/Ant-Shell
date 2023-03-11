SPLASH_ASCII = """
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 
                                                                              
                                                                              
     █████  ███    ██ ████████     ███████ ██   ██ ███████ ██      ██         
    ██   ██ ████   ██    ██        ██      ██   ██ ██      ██      ██         
    ███████ ██ ██  ██    ██        ███████ ███████ █████   ██      ██         
    ██   ██ ██  ██ ██    ██             ██ ██   ██ ██      ██      ██         
    ██   ██ ██   ████    ██        ███████ ██   ██ ███████ ███████ ███████    
                                                                              
                                                                              
    Version: x.x.x
                                                                              
█████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ █████ 
                                                                              
"""

from TkTerm.tkterm import *
from AntInterpreter import AntInterpreter

root = tk.Tk()
root.title("Ant Shell")
root.geometry("700x400")

terminal = Terminal(root, text=SPLASH_ASCII)
terminal.pack(fill=BOTH, expand=True)

interpreter = AntInterpreter()
terminal.add_interpreter("Ant", interpreter, set_default=True)

root.mainloop()