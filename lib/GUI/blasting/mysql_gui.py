# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
from conf import config  # 配置文件

def mysql_scanning(self):
    ssh_top = tk.Tk()
    ssh_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    ssh_top.title('Mysql破解')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    fofa_sbar = tk.Scrollbar(ssh_top,
                             background="#00FA9A",
                             activebackground="#00FA9A",
                             troughcolor="#363636",
                             borderwidth=-2,
                             activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    fofa_sbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # 设置文本框控件
    self.mysql_result = ttk.Text(ssh_top,
                                 yscrollcommand=fofa_sbar.set,  # 调用滚动条
                                 undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.mysql_result.place(relwidth=0.988,
                            relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.mysql_result.config(font=font,
                             foreground='#008B00')  # 颜色

    fofa_sbar.config(command=self.mysql_result.yview)  # 设置鼠标可以
    # for i in range(30):
    #     self.fofa_result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )

    try:
        self.mysql_result.edit_undo()  # 清空内容
    except:
        pass
    from blasting.mysql_blasting import mysql
    # self.Python_Awvs_result.insert(tk.END,self.awvs_xray_dd_cbox.get())
    # python_awvs.main_xray_dd()
    t = threading.Thread(target=mysql.gui, args=(self.mysql_host.get(),
                                                 self.mysql_port.get(),
                                                 self.mysql_thread.get(),
                                                 self.mysql_user.get(),
                                                 self.mysql_passwd.get(),
                                                 self.mysql_result))
    # 启动线程
    t.start()

    ssh_top.mainloop()
def mysql(self,top):

    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '\n\n说明！\nMysql多线程破解\n默认用户和密码字典可以在config.py文件进行修改')
    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="Mysql爆破",
                                bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边
    # ftp主机地址
    ttk.Label(fofa_right,
              text="主机地址：",
              bootstyle="success").grid(row=2, column=1, sticky=tk.W)

    # ftp主机地址
    # 生成动态字符串
    self.mysql_host = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.mysql_host,
              bootstyle="success",
              width=30).grid(row=2,
                             column=2,
                             sticky=tk.W)

    # 用户字典
    ttk.Label(fofa_right,
              text="用户字典：",
              bootstyle="success").grid(row=3, column=1, sticky=tk.W)

    self.mysql_user = tk.StringVar()
    mysql_user = ttk.Entry(fofa_right,
                         textvariable=self.mysql_user,
                         bootstyle="success",
                         width=30)
    mysql_user.grid(row=3,
                  column=2,
                  pady=10,
                  sticky=tk.W)
    mysql_user.insert(0, 'dictionary/mysql/user.txt')
    # 选择文件
    Backupfilescan_document = tk.Button(fofa_right,
                                        text='选择文件',
                                        relief=tk.RAISED,
                                        command=self.ssh_user_many)
    Backupfilescan_document.grid(row=3,
                                 column=3,
                                 sticky=tk.W)

    # 密码字典
    ttk.Label(fofa_right,
              text="密码字典：",
              bootstyle="success").grid(row=4, column=1, sticky=tk.W)
    self.mysql_passwd = tk.StringVar()
    mysql_passwd = ttk.Entry(fofa_right,
                           textvariable=self.mysql_passwd,
                           bootstyle="success",
                           width=30)

    mysql_passwd.grid(row=4,
                    column=2,
                    pady=10,
                    sticky=tk.W)
    mysql_passwd.insert(0, "dictionary/ssh/passwd.txt")

    # 选择文件
    passwd_file = tk.Button(fofa_right,
                            text='选择文件',
                            relief=tk.RAISED,
                            command=self.mysql_passwd_many)
    passwd_file.grid(row=4,
                     column=3,
                     sticky=tk.W)
    # 端口
    ttk.Label(fofa_right,
              text="端口：",
              bootstyle="success").grid(row=3, column=4, sticky=tk.W)

    # 端口
    # 生成动态字符串
    self.mysql_port = tk.StringVar()
    mysql_port = ttk.Entry(fofa_right, textvariable=self.mysql_port, bootstyle="success", width=10)
    mysql_port.grid(row=3, column=5, sticky=tk.W)
    mysql_port.insert(0, '3306')

    # 端口
    ttk.Label(fofa_right,
              text="线程数：",
              bootstyle="success").grid(row=4, column=4, sticky=tk.W)

    # 端口
    # 生成动态字符串
    self.mysql_thread = tk.StringVar()
    mysql_thread = ttk.Entry(fofa_right, textvariable=self.mysql_thread, bootstyle="success", width=10)
    mysql_thread.grid(row=4, column=5, sticky=tk.W)
    mysql_thread.insert(0, '5')

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.mysql_scanning)
    label_1.grid(row=2, column=6)  # 位置