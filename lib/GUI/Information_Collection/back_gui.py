# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
#sys.path.append("../../") # 解决上级库文件
from conf import config  # 配置文件


def back_scanning(self):
    back_top = tk.Tk()
    back_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    back_top.title('后台扫描')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    back_sbar = tk.Scrollbar(back_top,
                             background="#00FA9A",
                             activebackground="#00FA9A",
                             troughcolor="#363636",
                             borderwidth=-2,
                             activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    back_sbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # 设置文本框控件
    self.back_result = ttk.Text(back_top,
                                yscrollcommand=back_sbar.set,  # 调用滚动条
                                undo=True)  # 开启删除内容

    # 在主窗口内显示
    self.back_result.place(relwidth=0.988,
                           relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.back_result.config(font=font, foreground='#008B00')  # 颜色

    back_sbar.config(command=self.back_result.yview)  # 设置鼠标可以

    for i in range(30):
        self.back_result.insert(tk.END,
                                '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
                                    i + 1) + '次\n')
    try:
        # pass
        self.back_result.edit_undo()  # 清空内容
    except:
        pass

    from Initiative.backgroundscan import back

    # self.back_result.insert(tk.END,self.back_url.get())
    # self.back_result.insert(tk.END,self.back_t.get())

    # 定义线程 预防卡
    t = threading.Thread(target=back.GUI, args=(
    self.back_url.get(), self.back_t.get(), self.back_dictionary.get(), self.back_result, self.back_batch.get()))
    # 启动线程
    t.start()

    back_top.mainloop()


def back_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass

    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n本工具是一个后台扫描器\n支持多线程，批量扫描，可以指定字典默认指定字典默认是用的php.txt \n注意可选参数可以不用填，使用默认的')
    # 显示线
    fofa_right = ttk.LabelFrame(top, text="后台扫描器", bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边

    # 显示目标
    ttk.Label(fofa_right, text="目标URL：", bootstyle="success").grid(row=2, column=1, sticky=tk.W, padx=25)

    # 输入目标
    # 生成动态字符串
    self.back_url = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.back_url, bootstyle="success", width=30).grid(row=2, column=2, sticky=tk.W)

    # 指定线程
    ttk.Label(fofa_right, text=" 指定线程：", bootstyle="success").grid(row=2, column=3, sticky=tk.W)
    # 指定线程
    # 生成动态字符串
    self.back_t = tk.StringVar()
    back_t = ttk.Entry(fofa_right, textvariable=self.back_t, bootstyle="success", width=10)
    back_t.grid(row=2, column=4, sticky=tk.W)
    back_t.insert(0, 30)

    # 显示可选参数
    ttk.Label(fofa_right, text="可选参数：", bootstyle="success").grid(row=3, column=1, sticky=tk.W)

    # 文件批量扫描
    ttk.Label(fofa_right, text="文件批量扫描：", bootstyle="success").grid(row=4, column=1, sticky=tk.W, padx=25)
    # 指定文件批量扫描
    # 生成动态字符串
    self.back_batch = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.back_batch, bootstyle="success", width=30).grid(row=4, column=2,
                                                                                            sticky=tk.W)

    # 指定字典
    ttk.Label(fofa_right, text="指定字典：", bootstyle="success").grid(row=4, column=3, sticky=tk.W)
    # 指定字典
    # 生成动态字符串
    self.back_dictionary = tk.StringVar()
    back_dictionary = ttk.Entry(fofa_right, textvariable=self.back_dictionary, bootstyle="success", width=30)
    back_dictionary.grid(row=4, column=4, sticky=tk.W)
    back_dictionary.insert(0, './dictionary/back/PHP.txt')

    # 显示设置代理
    ttk.Label(fofa_right, text="代理IP：", bootstyle="success").grid(row=5, column=1, sticky=tk.W, padx=25, pady=25)

    # 显示设置代理
    self.back_h = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.back_h, bootstyle="success", width=30).grid(row=5, column=2, sticky=tk.W)

    ttk.Label(fofa_right, text="", bootstyle="success").grid(row=5, column=3, sticky=tk.W)
    # 指定页数
    # 生成动态字符串
    self.back_p = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.back_p, bootstyle="success", width=10).grid(row=5, column=4, sticky=tk.W)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.back_scanning)
    label_1.grid(row=2, column=5)  # 位置