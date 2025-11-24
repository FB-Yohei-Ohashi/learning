import tkinter as tk
from tkinter import ttk


def bt1():
    print(f"ボタンが押されました: {text_input1.get()}")


root = tk.Tk()
root.title("サンプルアプリ")
root.update()
root.lift()
root.focus_force()

root.geometry("300x400")

# フレーム１
frame1 = ttk.Frame(root)
frame1.grid(row=0, column=0)

# ラベル
label1 = ttk.Label(frame1, text="サンプルテキスト")
label1.pack()

# ボタン
button1 = ttk.Button(frame1, text="ボタン1", command=bt1)
button1.pack()

# エントリー
text_input1 = tk.StringVar()
entry1 = ttk.Entry(frame1, textvariable=text_input1)
entry1.pack()

# チェックボックス
input1 = tk.StringVar()
checkbox1 = ttk.Checkbutton(frame1, textvariable=input1)
checkbox1.pack()

# スケール
input2 = tk.DoubleVar()
scale1 = ttk.Scale(frame1, variable=input1, length=200, from_=0, to=99)
scale1.pack()

root.mainloop()
