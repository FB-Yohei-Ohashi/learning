import os
import tkinter as tk
from tkinter import filedialog, ttk


def bt1():
    # file_type = [("データ", "*.xlsx")]
    base_dir = os.path.abspath(os.path.dirname(__file__))
    # file_path = filedialog.askopenfilename(filetypes=file_type, initialdir=base_dir)
    dir_path = filedialog.askdirectory(initialdir=base_dir)

    text_input1.set(dir_path)


root = tk.Tk()
root.title("サンプルアプリ")
root.update()
root.lift()
root.focus_force()

root.geometry("300x400")

# フレーム１
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)

# ボタン
button1 = ttk.Button(frame1, text="ボタン1", command=bt1)
button1.pack()

# エントリー
text_input1 = tk.StringVar()
entry1 = ttk.Entry(frame1, textvariable=text_input1)
entry1.pack()

root.mainloop()
