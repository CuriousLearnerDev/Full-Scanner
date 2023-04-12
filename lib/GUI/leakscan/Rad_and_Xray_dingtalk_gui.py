# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件
from conf import config  # 配置文件


def Rad_and_Xray_dingtalk_invoke(self):
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
    self.Rad_and_Xray_dingtalk_result = ttk.Text(Backupfilescan_top,
                                                 yscrollcommand=Backupfilescan_sbar.set,  # 调用滚动条
                                                 undo=True)  # 开启删除内容

    # 在主窗口内显示
    self.Rad_and_Xray_dingtalk_result.place(relwidth=0.988,
                                            relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.Rad_and_Xray_dingtalk_result.config(font=font, foreground='#008B00')  # 颜色

    Backupfilescan_sbar.config(command=self.Rad_and_Xray_dingtalk_result.yview)  # 设置鼠标可以

    for i in range(30):
        self.Rad_and_Xray_dingtalk_result.insert(tk.END,
                                                 '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
                                                     i + 1) + '次\n')

    try:
        self.Rad_and_Xray_dingtalk_result.edit_undo()  # 清空内容
    except:
        pass

    from leakscan.rad_xray_py import rad_xray
    # 定义线程 预防卡
    t = threading.Thread(target=rad_xray.main_dingtalk_gui, args=(self.Rad_Xray_dingtalk_batch.get(),
                                                                  self.Rad_Xray_token.get(),
                                                                  self.Rad_and_Xray_dingtalk_result))
    # 启动线程
    t.start()

    Backupfilescan_top.mainloop()


def Rad_and_Xray_dingtalk(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '\n\n说明！\nRad联动Xray漏洞扫描目前只支持amd_linux\n钉钉信息推送可选！\n如果不想每次都配置钉钉的token可以去config配置文件添加')

    # 显示线
    fofa_right = ttk.LabelFrame(top, text="批量扫描Rad联动Xray联动钉钉推送", bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边

    # 显示目标
    ttk.Label(fofa_right,
              text="批量扫描地址：",
              bootstyle="success").grid(row=0,
                                        column=1,
                                        sticky=tk.W,
                                        pady=20)

    # 批量扫描
    # 生成动态字符串
    self.Rad_Xray_dingtalk_batch = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.Rad_Xray_dingtalk_batch,
              bootstyle="success",
              width=30).grid(row=0,
                             column=2,
                             sticky=tk.W,
                             pady=20)

    Rad_Xray_many = tk.Button(fofa_right,
                              text='选择文件',
                              relief=tk.RAISED,
                              command=self.Rad_and_Xray_dingtalk_many)

    Rad_Xray_many.grid(row=0,
                       column=3,
                       sticky=tk.W,
                       pady=20)

    # 显示目标
    ttk.Label(fofa_right,
              text="钉钉推送的token：",
              bootstyle="success").grid(row=1,
                                        column=1,
                                        sticky=tk.W,
                                        pady=20)
    # 输入目标
    # 生成动态字符串
    self.Rad_Xray_token = tk.StringVar()
    Rad_and_Xray_dingtalk_token=ttk.Entry(fofa_right,
                                          textvariable=self.Rad_Xray_token,
                                          bootstyle="success",
                                          width=30)
    Rad_and_Xray_dingtalk_token.grid(row=1,
                                     column=2,
                                     sticky=tk.W,
                                     pady=20)
    Rad_and_Xray_dingtalk_token.insert(0,config.SeriousConfig['dingtalk'])


    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.Rad_and_Xray_dingtalk_invoke)
    label_1.grid(row=0, column=4, pady=20, padx=50)  # 位置