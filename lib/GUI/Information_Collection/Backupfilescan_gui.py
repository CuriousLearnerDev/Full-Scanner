# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件



def Backupfilescan_scanning(self):
    Backupfilescan_top = tk.Tk()
    Backupfilescan_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    Backupfilescan_top.title('备份文件扫描')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    Backupfilescan_sbar = tk.Scrollbar(Backupfilescan_top,
                                       background="#00FA9A",
                                       activebackground="#00FA9A",
                                       troughcolor="#363636",
                                       borderwidth=-2,
                                       activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    Backupfilescan_sbar.pack(side=tk.RIGHT,
                             fill=tk.Y)

    # 设置文本框控件
    self.Backupfilescan_result = ttk.Text(Backupfilescan_top,
                                          yscrollcommand=Backupfilescan_sbar.set,  # 调用滚动条
                                          undo=True)  # 开启删除内容

    # 在主窗口内显示
    self.Backupfilescan_result.place(relwidth=0.988,
                                     relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.Backupfilescan_result.config(font=font, foreground='#008B00')  # 颜色

    Backupfilescan_sbar.config(command=self.Backupfilescan_result.yview)  # 设置鼠标可以

    for i in range(30):
        self.Backupfilescan_result.insert(tk.END,
                                          '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
                                              i + 1) + '次\n')

    try:
        self.Backupfilescan_result.edit_undo()  # 清空内容
    except:
        pass
    from Initiative.Backupfilescan import ProbeBackup
    # 定义线程 预防卡
    t = threading.Thread(target=ProbeBackup.GUI, args=(self.Backupfilescan_url.get(),
                                                       self.Backupfilescan_many.get(),
                                                       self.Backupfilescan_thread.get(),
                                                       self.Backupfilescan_document.get(),
                                                       self.Backupfilescan_proxies.get(),
                                                       self.Backupfilescan_result))
    # 启动线程
    t.start()

    # self.Backupfilescan_result.insert(tk.END,"目标URL"+self.Backupfilescan_url.get())

    Backupfilescan_top.mainloop()





def Backupfilescan_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass

    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n本工具是一个备份扫描工具可以批量目标扫描\n默认是用的自己生成的站长常见的备份方式\n可以指定字典\n注意可选参数可以不用填，使用默认的')
    # 显示线
    fofa_right = ttk.LabelFrame(top, text="备份文件扫描", bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边

    # 显示目标
    ttk.Label(fofa_right, text="目标URL：", bootstyle="success").grid(row=2, column=1, sticky=tk.W, padx=25)

    # 输入目标
    # 生成动态字符串
    self.Backupfilescan_url = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.Backupfilescan_url, bootstyle="success", width=30).grid(row=2, column=2,
                                                                                                    sticky=tk.W)

    # 显示
    ttk.Label(fofa_right, text=" 指定线程：", bootstyle="success").grid(row=2, column=3, sticky=tk.W)

    # 指定线程
    # 生成动态字符串
    self.Backupfilescan_thread = tk.StringVar()
    Backupfilescan_t = ttk.Entry(fofa_right, textvariable=self.Backupfilescan_thread, bootstyle="success", width=10)
    Backupfilescan_t.grid(row=2, column=4, sticky=tk.W)
    Backupfilescan_t.insert(0, 1)

    # 可选参数
    ttk.Label(fofa_right, text="可选参数：", bootstyle="success").grid(row=3, column=1, sticky=tk.W)

    # 文件批量扫描
    ttk.Label(fofa_right, text="文件批量扫描：", bootstyle="success").grid(row=4, column=1, sticky=tk.W, padx=25)
    # 文件批量扫描
    # 生成动态字符串
    self.Backupfilescan_many = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.Backupfilescan_many, bootstyle="success", width=30).grid(row=4, column=2,
                                                                                                     sticky=tk.W)
    Backupfilescan_many = tk.Button(fofa_right,
                                    text='选择文件',
                                    relief=tk.RAISED,
                                    command=self.askfile_many)
    Backupfilescan_many.grid(row=4,
                             column=3,
                             sticky=tk.W)

    # 字典
    ttk.Label(fofa_right, text="指定字典：", bootstyle="success").grid(row=4, column=4, sticky=tk.W)

    # 指定字典
    # 生成动态字符串
    self.Backupfilescan_document = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.Backupfilescan_document, bootstyle="success", width=30).grid(row=4,
                                                                                                         column=5,
                                                                                                         sticky=tk.W)

    # 选择文件
    Backupfilescan_document = tk.Button(fofa_right,
                                        text='选择文件',
                                        relief=tk.RAISED,
                                        command=self.askfile_document)
    Backupfilescan_document.grid(row=4,
                                 column=6,
                                 sticky=tk.W)

    # 显示设置代理
    ttk.Label(fofa_right, text="代理IP：", bootstyle="success").grid(row=5, column=1, sticky=tk.W, padx=25, pady=25)

    # 显示设置代理
    # 生成动态字符串
    self.Backupfilescan_proxies = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.Backupfilescan_proxies, bootstyle="success", width=30).grid(row=5, column=2,
                                                                                                        sticky=tk.W)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始扫描",
                         bootstyle="success",
                         width=20,
                         command=self.Backupfilescan_scanning)
    label_1.grid(row=2, column=5)  # 位置467

    # ---------------------信息收集备份文件扫描模块---------------------