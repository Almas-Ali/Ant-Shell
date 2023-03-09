from TkTerm.tkterm import *

root = tk.Tk()
root.title("Ant Terminal")
root.geometry("700x400")

terminal = Terminal(root)
terminal.pack(fill=BOTH, expand=True)

root.mainloop()