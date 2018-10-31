# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import tkinter as tk


from center_window import *


def rules():
    top = tk.Tk()
    top.title('五子棋规则')
    center_window(top, 433, 647)
    with open('rule.txt', 'r') as f:
        texts = '\n' * 5
        while True:
            msg = f.readline()
            if not msg:
                break
            texts += msg + '\n'
    photo = tk.PhotoImage(file="img/rule.png")
    theLabels = tk.Label(top,
                         text=texts,  # 内容
                         justify=tk.LEFT,  # 对齐方式
                         image=photo,  # 加入图片
                         compound=tk.CENTER,  # 关键:设置为背景图片
                         font=("华文行楷", 14),  # 字体和字号
                         fg="green")  # 前景色
    theLabels.pack()
    tk.mainloop()
