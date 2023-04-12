# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件



def google_scanning(self,top):
    google_top = tk.Tk()
    google_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    google_top.title('google爬虫')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    google_sbar = tk.Scrollbar(google_top,
                               background="#00FA9A",
                               activebackground="#00FA9A",
                               troughcolor="#363636",
                               borderwidth=-2,
                               activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    google_sbar.pack(side=tk.RIGHT,
                     fill=tk.Y)

    # 设置文本框控件
    self.google_result = ttk.Text(google_top,
                                  yscrollcommand=google_sbar.set,  # 调用滚动条
                                  undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.google_result.place(relwidth=0.988,
                             relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.google_result.config(font=font, foreground='#008B00')  # 颜色

    google_sbar.config(command=self.google_result.yview)  # 设置鼠标可以
    for i in range(30):
        self.google_result.insert(tk.END,
                                  '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
                                      i + 1) + '次\n')

    try:
        self.google_result.edit_undo()  # 清空内容
    except:
        pass
    from collect import google
    proxy = (self.google_h.get() + ':' + self.google_p.get())
    # 定义线程对象a函数
    duix1 = threading.Thread(target=google.GUI,
                             args=(self.google_url.get(),
                                   proxy,
                                   self.google_number.get(),
                                   self.google_result))
    # 启动线程
    duix1.start()

    google_top.mainloop()

def google_passive_information_gathering(self,top):

    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass

    # 这个模块说明
    self.illustrate.insert(ttk.END,
                       '说明！\n 搜索引擎爬虫\n 比如输入 intitle:后台登陆 "学院"\n注意：提取的页数如果不指定默认就是100000')

    # 显示线
    google_right = ttk.LabelFrame(top,
                                text="google爬虫",
                                bootstyle="success")
    google_right.place(relx = 0.21,  # 左边
                     rely=0.1,# 上边
                     relwidth=0.785, # 右边
                     relheight=0.3) # 下边
    # 显示目标
    ttk.Label(google_right,
              text="查询目标：",
              bootstyle="success").grid(row=2,
                                        column=1,
                                        sticky=tk.W,
                                        padx=25)

    # 输入目标
    # 生成动态字符串
    self.google_url = tk.StringVar()
    ttk.Entry(google_right,
              textvariable=self.google_url,
              bootstyle="success",
              width=30).grid(row=2,
                             column=2,
                             sticky=tk.W)

    # 显示可选参数
    ttk.Label(google_right,
              text="设置代理：",
              bootstyle="success").grid(row=3,
                                        column=1,
                                        sticky=tk.W,
                                        padx=25)

    # 显示设置代理
    ttk.Label(google_right,
              text="代理IP：",
              bootstyle="success").grid(row=4,
                                        column=1,
                                        sticky=tk.W,
                                        padx=25)


    # 设置指定页数
    # 生成动态字符串
    self.google_h = tk.StringVar()
    google_p = ttk.Entry(google_right,
                         textvariable=self.google_h,
                         bootstyle="success",
                         width=30)
    google_p.grid(row=4,
                  column=2,
                  sticky=tk.W)
    google_p.insert(0, '127.0.0.1')

    # 显示
    ttk.Label(google_right,
              text=" 代理端口：",
              bootstyle="success").grid(row=4,
                                        column=3,
                                        sticky=tk.W)
    # 指定页数
    # 生成动态字符串
    self.google_p = tk.StringVar()
    ttk.Entry(google_right,
              textvariable=self.google_p,
              bootstyle="success",
              width=10).grid(row=4,
                             column=4,
                             sticky=tk.W)

    # 显示
    ttk.Label(google_right,
              text=" 页数(默认100000)：",
              bootstyle="success").grid(row=6,
                                        column=1,
                                        sticky=tk.W,
                                        padx=25)
    # 指定页数
    # 生成动态字符串
    self.google_number = tk.StringVar()
    google_n = ttk.Entry(google_right,
                         textvariable=self.google_number,
                         bootstyle="success")
    google_n.grid(row=6,
                  column=2,
                  sticky=tk.W,
                  pady=25)
    google_n.insert(0, 100000)

    # 按钮开始
    label_1 = ttk.Button(google_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.google_scanning)
    label_1.grid(row=2, column=4)  # 位置