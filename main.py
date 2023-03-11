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
root.title("Ant Terminal")
root.geometry("700x400")

terminal = Terminal(root, bd=0, text=SPLASH_ASCII)
terminal.pack(fill=BOTH, expand=True)

interpreter = AntInterpreter()
terminal.add_interpreter("Ant", interpreter, set_default=True)

root.mainloop()