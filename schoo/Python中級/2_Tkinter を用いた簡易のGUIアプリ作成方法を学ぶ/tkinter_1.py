import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("サンプルアプリ")
root.update()
root.lift()
root.focus_force()

root.geometry("300x400")

# フレーム１
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)
button1 = ttk.Button(frame1, text="ボタン1")
button1.pack()

# フレーム2
frame2 = ttk.Frame(root)
frame2.grid(row=1, column=1)
button2 = ttk.Button(frame2, text="ボタン2")
button2.pack()

# フレーム３
frame3 = ttk.Frame(root)
frame3.grid(row=2, column=0)
button3 = ttk.Button(frame3, text="ボタン3")
button3.pack()

root.mainloop()
