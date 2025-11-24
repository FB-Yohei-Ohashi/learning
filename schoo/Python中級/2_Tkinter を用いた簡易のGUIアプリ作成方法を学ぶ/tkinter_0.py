import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("サンプルアプリ")
root.update()
root.lift()
root.focus_force()

w = root.winfo_screenwidth()
h = root.winfo_screenheight()

root.geometry(f"{w}x{h}")

root.mainloop()