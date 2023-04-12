# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住


def Single_Rad_and_Xray_invoke(self):
    Backupfilescan_top = tk.Tk()
    Backupfilescan_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    Backupfilescan_top.title('Rad联动Xray进度')
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
    self.Single_Rad_and_Xray_result = ttk.Text(Backupfilescan_top,
                                               yscrollcommand=Backupfilescan_sbar.set,  # 调用滚动条
                                               undo=True)  # 开启删除内容

    # 在主窗口内显示
    self.Single_Rad_and_Xray_result.place(relwidth=0.988,
                                          relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.Single_Rad_and_Xray_result.config(font=font, foreground='#008B00')  # 颜色

    Backupfilescan_sbar.config(command=self.Single_Rad_and_Xray_result.yview)  # 设置鼠标可以

    for i in range(30):
        self.Single_Rad_and_Xray_result.insert(tk.END,
                                               '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
                                                   i + 1) + '次\n')

    try:
        self.Single_Rad_and_Xray_result.edit_undo()  # 清空内容
    except:
        pass

    from leakscan.rad_xray_py import rad_xray
    # 定义线程 预防卡
    t = threading.Thread(target=rad_xray.main_Single__gui, args=(self.Single_Rad_Xray_dingtalk_batch.get(),
                                                                 self.Single_Rad_and_Xray_result))
    # 启动线程
    t.start()

    Backupfilescan_top.mainloop()


def Single_Rad_and_Xray(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '\n\n说明！\nRad联动Xray漏洞扫描目前只支持amd_linux')

    # 显示线
    fofa_right = ttk.LabelFrame(top, text="单个扫描Rad联动Xray", bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边

    # 显示目标
    ttk.Label(fofa_right,
              text="单个扫描地址：",
              bootstyle="success").grid(row=2,
                                        column=1,
                                        sticky=tk.W,
                                        pady=40)

    # 批量扫描
    # 生成动态字符串
    self.Single_Rad_Xray_dingtalk_batch = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.Single_Rad_Xray_dingtalk_batch,
              bootstyle="success",
              width=30).grid(row=2,
                             column=2,
                             sticky=tk.W,
                             pady=40)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.Single_Rad_and_Xray_invoke)
    label_1.grid(row=2, column=4, sticky=tk.W, pady=40, padx=20)  # 位置
