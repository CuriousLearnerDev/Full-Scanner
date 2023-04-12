# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import messagebox

# 调用Tk()创建主窗口
top =tk.Tk()

top.geometry('450x400+300+200')

# 给主窗口起一个名字，也就是窗口的名字
top.title('赵赛赛')

# 设置回调函数
def callback():
    messagebox.showinfo('你输入的是', dstr.get())

# 生成动态字符串
dstr = tk.StringVar()

# 利用 textvariable 来实现文本变化
lb = tk.Entry(top,textvariable=dstr)

# 将按钮放置在主窗口内
lb.pack()

lb.insert(0,'这个是默认值')


b=tk.Button(top, text="登录", command=callback)
b.pack()

#开启主循环，让窗口处于显示状态
top.mainloop()