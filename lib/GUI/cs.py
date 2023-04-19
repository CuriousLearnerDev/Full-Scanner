# -*- coding:utf-8 -*-
import tkinter as tk
from PIL.ImageTk import PhotoImage
import ttkbootstrap as ttk
import threading  # 预防卡住
import sys
import os
import shutil
from conf import config  # 配置文件

from ttkbootstrap.constants import *
#import Coding_tools
#import Utilities
from lib.GUI import Coding_tools
from lib.GUI import Utilities
from tkinter import filedialog  # 注意次数要将文件对话框导入



# 信息收集模块
#sys.path.append("lib/GUI/") # 解决上级库文件
from lib.GUI.Information_Collection  import fofa_gui
from lib.GUI.Information_Collection import bing_gui
from lib.GUI.Information_Collection import google_gui
from lib.GUI.Information_Collection import whois_gui
from lib.GUI.Information_Collection import shodan_gui
from lib.GUI.Information_Collection import Port_scanning_gui
from lib.GUI.Information_Collection import SubDns_gui
from lib.GUI.Information_Collection import Backupfilescan_gui
from lib.GUI.Information_Collection import back_gui



# 漏洞扫描
from lib.GUI.leakscan import Rad_and_Xray_dingtalk_gui
from lib.GUI.leakscan import Rad_and_Xray_gui
from lib.GUI.leakscan import Single_Rad_and_Xray_gui
from lib.GUI.leakscan import Python_Awvs_gui

# 爆破
from lib.GUI.blasting import ftp_gui
from lib.GUI.blasting import ssh_gui
from lib.GUI.blasting import mysql_gui
from lib.GUI.blasting import crack_gui


import time


class interface:

    # ---------------------信息收集FOFA模块---------------------
    def fofa_scanning(self):
        fofa_gui.fofa_scanning(self,top)

    def fofa_passive_information_gathering(self):
        fofa_gui.fofa_passive_information_gathering(self,top)

    # ---------------------信息收集FOFA模块---------------------


    # ---------------------信息收集bing爬虫模块---------------------

    def bing_scanning(self):
        bing_gui.bing_scanning(self,top)

    def bing_passive_information_gathering(self):
        bing_gui.bing_passive_information_gathering(self,top)

    # ---------------------信息收集bing爬虫模块---------------------

    # ---------------------信息收集google爬虫模块---------------------
    def google_scanning(self):
        google_gui.google_scanning(self,top)

    def google_passive_information_gathering(self):
        google_gui.google_passive_information_gathering(self,top)


    # ---------------------信息收集google爬虫模块---------------------

    # ---------------------信息收集whois查询模块---------------------
    def whois_scanning(self):
        whois_gui.whois_scanning(self)


    def whois_passive_information_gathering(self):
        whois_gui.whois_passive_information_gathering(self,top)

    # ---------------------信息收集whois查询模块---------------------

    # ---------------------信息收集shodan收集模块---------------------
    def shodan_scanning(self):
        shodan_gui.shodan_scanning(self)

    def shodan_passive_information_gathering(self):
        shodan_gui.shodan_passive_information_gathering(self,top)


    # ---------------------信息收集shodan收集模块---------------------、

    # ---------------------信息收集端口扫描模块---------------------
    def port_scanning(self):
        Port_scanning_gui.port_scanning(self)

    def port_passive_information_gathering(self):
        Port_scanning_gui.port_passive_information_gathering(self,top)


    # ---------------------信息收集端口扫描模块---------------------

    # ---------------------信息收集CMS识别模块---------------------

    def cms_passive_information_gathering(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass
        # 这个模块说明
        self.illustrate.insert(ttk.END,
                               '说明！\n请使用命令行的或者选择模式\n这个cms识别不是本人写的里面的要是改图形化的我得大改呜呜呜呜！')

        # 显示线
        fofa_right = ttk.LabelFrame(top, text="CMS识别", bootstyle="success")
        fofa_right.place(relx = 0.21,  # 左边
                         rely=0.1,# 上边
                         relwidth=0.785, # 右边
                         relheight=0.3) # 下边
    # ---------------------信息收集CMS识别模块---------------------

    # ---------------------信息收集子域名探测模块---------------------

    def SubDns_scanning(self):
        SubDns_gui.SubDns_scanning(self)

    def SubDns_passive_information_gathering(self):
        SubDns_gui.SubDns_passive_information_gathering(self,top)
    # ---------------------信息收集子域名探测模块---------------------


    # ---------------------信息收集备份文件扫描模块---------------------

    # 定义一个处理文件的相关函数
    def askfile_document(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()
        self.Backupfilescan_document.set(filename)

    # 定义一个处理文件的相关函数
    def askfile_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()
        self.Backupfilescan_many.set(filename)
    def Backupfilescan_scanning(self):
        Backupfilescan_gui.Backupfilescan_scanning(self)


    def Backupfilescan_passive_information_gathering(self):
        Backupfilescan_gui.Backupfilescan_passive_information_gathering(self,top)


    # ---------------------信息收集备份文件扫描模块---------------------

    # ---------------------信息收集后台扫描模块---------------------
    def back_scanning(self):
        back_gui.back_scanning(self)


    def back_passive_information_gathering(self):
        back_gui.back_passive_information_gathering(self,top)


    # ---------------------信息收集后台扫描模块---------------------


    # ---------------------FTP破解---------------------
    def ftp_user_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename1 = filedialog.askopenfilename()
        self.ftp_user.set(filename1)

    def ftp_passwd_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename2 = filedialog.askopenfilename()
        self.ftp_passwd.set(filename2)

    def Ftp_scanning(self):
        ftp_gui.Ftp_scanning(self)
    def Ftp(self):
        ftp_gui.Ftp(self,top)

    # ---------------------FTP破解---------------------
    # ---------------------SSH破解---------------------
    def ssh_user_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename1 = filedialog.askopenfilename()
        self.ssh_user.set(filename1)

    def ssh_passwd_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename2 = filedialog.askopenfilename()
        self.ssh_passwd.set(filename2)

    def ssh_scanning(self):
        ssh_gui.ssh_scanning(self)
    def ssh(self):
        ssh_gui.ssh(self,top)
    # ---------------------SSH破解---------------------


    # ---------------------mysql破解---------------------
    def mysql_user_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename1 = filedialog.askopenfilename()
        self.mysql_user.set(filename1)

    def mysql_passwd_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename2 = filedialog.askopenfilename()
        self.mysql_passwd.set(filename2)

    def mysql_scanning(self):
        mysql_gui.mysql_scanning(self)

    def mysql(self):

        mysql_gui.mysql(self,top)

    # ---------------------mysql破解---------------------

    # ---------------------web登录破解---------------------
    def crack_scanning(self):
        crack_gui.crack_scanning(self)

    def crack(self):
        crack_gui.crack(self,top)

    # ---------------------web登录破解---------------------


    # ---------------------信息收集模块---------------------
    def information_gathering(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass
        # 这个模块说明
        self.illustrate.insert(ttk.END,
                             '\n信息探测')
        # 显示线
        fofa_right = ttk.LabelFrame(top, text="信息收集模块", bootstyle="secondary")
        fofa_right.place(rely=0.1,# 上边
                         relwidth=1, # 右边
                         relheight=1) # 下边

        self.scan_result()

        frame_right = ttk.LabelFrame(top, text="信息收集模块", bootstyle="success")
        frame_right.place(rely=0.1,# 上边
                          relwidth=0.2, # 右边
                          relheight=1.0) # 下边

        label_1 = ttk.Button(frame_right,
                             text="fofa搜索结果提取",
                             bootstyle="success-outline",
                             width=28,
                             command=self.fofa_passive_information_gathering)
        label_1.grid(row=1,
                     column=1,
                     pady=9,)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="shodan信息收集",
                             bootstyle="success-outline",
                             width=28,
                             command=self.shodan_passive_information_gathering)
        label_1.grid(row=2,
                     column=1,
                     pady=9)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="whois查询",
                             bootstyle="success-outline",
                             width=28,
                             command=self.whois_passive_information_gathering)
        label_1.grid(row=3,
                     column=1,
                     pady=9)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="bing搜索引擎爬虫",
                             bootstyle="success-outline",
                             command=self.bing_passive_information_gathering,
                             width=28)
        label_1.grid(row=4,
                     column=1,
                     pady=9)  # 位置
        label_1 = ttk.Button(frame_right,
                             text="google搜索引擎爬虫",
                             bootstyle="success-outline",
                             width=28,
                             command=self.google_passive_information_gathering)
        label_1.grid(row=5,
                     column=1,
                     pady=10)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="子域名查询",
                             bootstyle="success-outline",
                             width=28,
                             command=self.SubDns_passive_information_gathering)
        label_1.grid(row=6,
                     column=1,
                     pady=10)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="端口扫描",
                             bootstyle="success-outline",
                             width=28,
                             command=self.port_passive_information_gathering)
        label_1.grid(row=7,
                     column=1,
                     pady=10)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="目标cms识别",
                             bootstyle="success-outline",
                             width=28,
                             command=self.cms_passive_information_gathering)
        label_1.grid(row=8,
                     column=1,
                     pady=10)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="备份文件扫描",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Backupfilescan_passive_information_gathering)
        label_1.grid(row=9,
                     column=1,
                     pady=10)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="后台扫描",
                             bootstyle="success-outline",
                             width=28,
                             command=self.back_passive_information_gathering)

        label_1.grid(row=10,
                     column=1,
                     pady=10)  # 位置


    # ---------------------信息收集模块---------------------


    # ---------------------批量Rad联动Xray联动钉钉---------------------
    # 定义一个处理文件的相关函数
    def Rad_and_Xray_dingtalk_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()
        self.Rad_Xray_dingtalk_batch.set(filename)

    def Rad_and_Xray_dingtalk_invoke(self):
        Rad_and_Xray_dingtalk_gui.Rad_and_Xray_dingtalk_invoke(self)

    def Rad_and_Xray_dingtalk(self):
        Rad_and_Xray_dingtalk_gui.Rad_and_Xray_dingtalk(self,top)


    # ---------------------批量Rad联动Xray联动钉钉---------------------

    # ---------------------批量Rad联动Xray---------------------
    # 定义一个处理文件的相关函数
    def Rad_and_Xray_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()
        self.Rad_Xray_batch.set(filename)


    def Rad_and_Xray_invoke(self):
        Rad_and_Xray_gui.Rad_and_Xray_invoke(self)

    def Rad_and_Xray(self):
        Rad_and_Xray_gui.Rad_and_Xray(self,top)

    # ---------------------批量Rad联动Xray---------------------

    # ---------------------单个Rad联动Xray---------------------


    def Single_Rad_and_Xray_invoke(self):
        Single_Rad_and_Xray_gui.Single_Rad_and_Xray_invoke(self)

    def Single_Rad_and_Xray(self):
        Single_Rad_and_Xray_gui.Single_Rad_and_Xray(self,top)


    # ---------------------单个Rad联动Xray---------------------


    # ---------------------Py调用AWVS联动Xray联动钉钉推送---------------------

    def Python_Awvs_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()

        self.awvs_xray_dd_file.set(filename)

    def Python_Awvs_scanning(self):
        Python_Awvs_gui.Python_Awvs_scanning(self)

    def Python_Awvs(self):
        Python_Awvs_gui.Python_Awvs(self,top)


    # ---------------------Py调用AWVS联动Xray联动钉钉推送---------------------

    # ---------------------Py调用AWVS---------------------
    def Python_Awvs_batch_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename = filedialog.askopenfilename()

        self.awvs_file.set(filename)


    def Python_Awvs_batch_scanning(self):
        Python_Awvs_batch_top = tk.Tk()
        Python_Awvs_batch_top.geometry('780x800')
        # 给主窗口起一个名字，也就是窗口的名字
        Python_Awvs_batch_top.title('Py调用AWVS联动Xray联动钉钉推送')
        # whois_top.config(background="#2F4F4F")

        # 创建一个滚动条控件，默认为垂直方向
        fofa_sbar = tk.Scrollbar(Python_Awvs_batch_top,
                                 background="#00FA9A",
                                 activebackground="#00FA9A",
                                 troughcolor="#363636",
                                 borderwidth=-2,
                                 activerelief='groove')

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        fofa_sbar.pack(side=tk.RIGHT,
                       fill=tk.Y)

        # 设置文本框控件
        self.awvs_result = ttk.Text(Python_Awvs_batch_top,
                                    yscrollcommand=fofa_sbar.set,  # 调用滚动条
                                    undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.awvs_result.place(relwidth=0.988,
                               relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font = tk.font.Font()
        self.awvs_result.config(font=font,
                                foreground='#008B00')  # 颜色

        fofa_sbar.config(command=self.awvs_result.yview)  # 设置鼠标可以
        # for i in range(30):
        #     self.fofa_result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )

        try:
            self.awvs_result.edit_undo()  # 清空内容
        except:
            pass
        from leakscan.awvs import python_awvs
        # self.Python_Awvs_result.insert(tk.END,self.awvs_xray_dd_cbox.get())
        # python_awvs.main_xray_dd()
        t = threading.Thread(target=python_awvs.main_gui, args=(self.awvs_url.get(),
                                                                    self.awvs_ApiKey.get(),
                                                                    self.awvs_file.get(),
                                                                    self.awvs_cbox.get(),
                                                                    self.awvs_Time.get(),
                                                                    self.awvs_name.get(),
                                                                    self.awvs_result))
        # 启动线程
        t.start()

        Python_Awvs_batch_top.mainloop()



    def Python_Awvs_batch(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass
        # 这个模块说明
        self.illustrate.insert(ttk.END,
                               '\n\n说明！\nPy调用AWVS联动Xray联动钉钉推送\n速度说明：slow(慢)、moderate(中)、fasts(快)\n钉钉推送的token，不想每次都添加可以去config配置文件里面添加')

        # 显示线
        fofa_right = ttk.LabelFrame(top,
                                    text="Py调用AWVS联动Xray联动钉钉推送",
                                    bootstyle="success")
        fofa_right.place(relx=0.21,  # 左边
                         rely=0.1,  # 上边
                         relwidth=0.785,  # 右边
                         relheight=0.3)  # 下边

        # 显示目标
        ttk.Label(fofa_right,
                  text="AWVS地址：",
                  bootstyle="success").grid(row=2, column=1, sticky=tk.W)

        # awvs的url
        # 生成动态字符串
        self.awvs_url = tk.StringVar()
        Awvs_Host = ttk.Entry(fofa_right, textvariable=self.awvs_url, bootstyle="success", width=30)
        Awvs_Host.grid(row=2, column=2, sticky=tk.W)
        Awvs_Host.insert(0, 'https://127.0.0.1:3443')

        # 指定线程
        ttk.Label(fofa_right,
                  text=" 扫描备注：",
                  bootstyle="success").grid(row=2, column=3, sticky=tk.W)
        # 扫描备注
        # 生成动态字符串
        self.awvs_name = tk.StringVar()
        Awvs_Name = ttk.Entry(fofa_right, textvariable=self.awvs_name, bootstyle="success", width=20)
        Awvs_Name.grid(row=2, column=4, sticky=tk.W)
        Awvs_Name.insert(0, 'Full-Scanner')

        # awvs的ApiKey
        ttk.Label(fofa_right,
                  text="ApiKey：",
                  bootstyle="success").grid(row=4, column=1, sticky=tk.W)
        # 指定awvs的ApiKey
        # 生成动态字符串
        self.awvs_ApiKey = tk.StringVar()
        awvs_ApiKey=ttk.Entry(fofa_right,
                  textvariable=self.awvs_ApiKey,
                  bootstyle="success",
                  width=30)
        awvs_ApiKey.grid(row=4, column=2, sticky=tk.W)
        awvs_ApiKey.insert(0,config.SeriousConfig['awvs'])
        # 指定文件批量扫描
        ttk.Label(fofa_right,
                  text="批量扫描文件：",
                  bootstyle="success").grid(row=4, column=3, sticky=tk.W)
        # 指定文件批量扫描
        # 生成动态字符串
        self.awvs_file = tk.StringVar()
        Awvs_back_dictionary = ttk.Entry(fofa_right, textvariable=self.awvs_file, bootstyle="success", width=30)
        Awvs_back_dictionary.grid(row=4, column=4, sticky=tk.W)

        # 选择文件
        Backupfilescan_document = tk.Button(fofa_right,
                                            text='选择文件',
                                            relief=tk.RAISED,
                                            command=self.Python_Awvs_batch_many)
        Backupfilescan_document.grid(row=4,
                                     column=5,
                                     sticky=tk.W)


        # ttk.Label(fofa_right,
        #           text="",
        #           bootstyle="success").grid(row=5, column=3, sticky=tk.W)

        # 多少秒添加
        ttk.Label(fofa_right,
                  text="多少秒添加：",
                  bootstyle="success").grid(row=5, column=3, sticky=tk.W)

        # 多少秒添加
        self.awvs_Time = tk.StringVar()
        Awvs_Time = ttk.Entry(fofa_right,
                              textvariable=self.awvs_Time,
                              bootstyle="success",
                              width=10)
        Awvs_Time.grid(row=5, column=4, sticky=tk.W)
        Awvs_Time.insert(0, '1200')

        # # 指定页数
        # # 生成动态字符串
        # self.back_p = tk.StringVar()
        # ttk.Entry(fofa_right,
        #           textvariable=self.back_p,
        #           bootstyle="success",
        #           width=10).grid(row=5, column=4,sticky=tk.W)
        # 显示设置代理

        # 扫描速度设置
        ttk.Label(fofa_right,
                  text="扫描速度设置：",
                  bootstyle="success").grid(row=5, column=1, sticky=tk.W)
        # 扫描速度设置
        self.awvs_cbox = ttk.Combobox(fofa_right, width=10)
        # 设置下拉菜单中的值
        self.awvs_cbox['value'] = ('slow', 'moderate', 'fasts')

        # 通过 current() 设置下拉菜单选项的默认值
        self.awvs_cbox.current(1)
        # 绑定下拉菜单事件
        self.awvs_cbox.bind("<<ComboboxSelected>>")
        self.awvs_cbox.grid(row=5, column=2, sticky=tk.W)

        # 按钮开始
        label_1 = ttk.Button(fofa_right,
                             text="开始",
                             bootstyle="success",
                             width=13,
                             command=self.Python_Awvs_batch_scanning)
        label_1.grid(row=2, column=5)  # 位置
    # ---------------------Py调用AWVS---------------------



    # ---------------------漏洞扫描模块---------------------
    def VulnerabilityScan(self):
        # 显示线
        fofa_right = ttk.LabelFrame(top, text="漏洞扫描模块", bootstyle="secondary")
        fofa_right.place(rely=0.1,# 上边
                         relwidth=1, # 右边
                         relheight=1) # 下边

        self.scan_result()




        frame_right = ttk.LabelFrame(top, text="漏洞扫描模块", bootstyle="success")
        frame_right.place(rely=0.1,# 上边
                          relwidth=0.2, # 右边
                          relheight=1.0) # 下边


        label_1 = ttk.Button(frame_right,
                             text="批量扫描Rad联动Xray联动钉钉推送",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Rad_and_Xray_dingtalk)
        label_1.grid(row=1,
                     column=1,
                     pady=9,)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="批量扫描Rad联动Xray",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Rad_and_Xray)
        label_1.grid(row=2,
                     column=1,
                     pady=9,)  # 位置

        label_1 = ttk.Button(frame_right,
                             text="单个扫描Rad联动Xray",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Single_Rad_and_Xray)
        label_1.grid(row=3,
                     column=1,
                     pady=9,)  # 位置



        label_1 = ttk.Button(frame_right,
                             text="Py调用AWVS联动Xray联动钉钉推送",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Python_Awvs)
        label_1.grid(row=4,
                     column=1,
                     pady=9, )  # 位置

        label_1 = ttk.Button(frame_right,
                             text="Python调用AWVS批量扫描",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Python_Awvs_batch)
        label_1.grid(row=5,
                     column=1,
                     pady=9, )  # 位置
    # ---------------------漏洞扫描模块---------------------
    # ---------------------小工具查询端口对应的服务模块---------------------

    def port_service_small_tools(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass

        # 这个模块说明
        self.illustrate.insert(ttk.END,
                               '说明！\n端口查询对应的服务')

    # ---------------------小工具查询端口对应的服务模块---------------------

    # ---------------------暴力破解模块---------------------
    def Brute_force_module(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass
        # 这个模块说明
        self.illustrate.insert(ttk.END,
                           '\n信息探测')
        # 显示线
        fofa_right = ttk.LabelFrame(top, text="暴力破解模块", bootstyle="secondary")
        fofa_right.place(rely=0.1,# 上边
                         relwidth=1,
                         relheight=1)

        self.scan_result()




        information_gathering_frame_right = ttk.LabelFrame(top, text="暴力破解模块", bootstyle="success")
        information_gathering_frame_right.place(rely=0.1,# 上边
                                              relwidth=0.2,
                                              relheight=1.0)

        label_1 = ttk.Button(information_gathering_frame_right,
                             text="FTP爆破",
                             bootstyle="success-outline",
                             width=28,
                             command=self.Ftp)
        label_1.grid(row=1,
                     column=1,
                     pady=9,)  # 位置

        label_1 = ttk.Button(information_gathering_frame_right,
                             text="SSH破解",
                             bootstyle="success-outline",
                             width=28,
                             command=self.ssh)
        label_1.grid(row=2,
                     column=1,
                     pady=9)  # 位置
        label_1 = ttk.Button(information_gathering_frame_right,
                             text="MYSQL破解",
                             bootstyle="success-outline",
                             width=28,
                             command=self.mysql)
        label_1.grid(row=3,
                     column=1,
                     pady=9)  # 位置


        label_1 = ttk.Button(information_gathering_frame_right,
                             text="登录界面破解",
                             bootstyle="success-outline",
                             width=28,
                             command=self.crack)
        label_1.grid(row=4,
                     column=1,
                     pady=9)  # 位置

    # ---------------------暴力破解模块---------------------


    # ---------------------编码工具模块---------------------

    def Coding(self):
        tool = Coding_tools.tool()
        tool.main(top)


    # ---------------------编码工具模块---------------------


    # ---------------------实用工具模块---------------------

    def Utilities(self):
        tool = Utilities.tool()
        tool.main(top)

    # ---------------------实用工具模块---------------------
    # ---------------------导入POCEXP---------------------
    def PocAndExpScript_many(self):
        # 从本地选择一个文件，并返回文件的目录
        filename1 = filedialog.askopenfilename()
        self.pocxep_file.set(filename1)


    # 添加POCEXP
    def Import_pocexp(self):
        print(self.pocxep_file.get())

        if self.pocxep_file.get()=="":
            pass
        else:
        # 复制文件
            shutil.copy(self.pocxep_file.get(), r'PocAndExpScript/generate/')

        # 更新POC
        from PocAndExpScript import main
        main.Interface(result=self.illustrate)

    # 清除POCEXP
    def purge_pocexp(self):
        # 更新POC
        from PocAndExpScript import main
        main.default(result=self.illustrate)

    # 检查已经添加的POCEXP
    def listdir(self):
        listdir = open('PocAndExpScript/storage.txt')
        frame_right = ttk.LabelFrame(top, text="已经导入的POCEXP", bootstyle="success")
        frame_right.place(rely=0.1,# 上边
                          relwidth=0.2, # 右边
                          relheight=1.0) # 下边

        for i in listdir:
            # 密码字典
            ttk.Label(frame_right,
                      text=i.rstrip(),
                      bootstyle="success").pack()


    def PocAndExpScript(self):
        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass

        # 显示线
        fofa_right = ttk.LabelFrame(top, text="导入POCEXP", bootstyle="secondary")
        fofa_right.place(rely=0.1,# 上边
                         relwidth=1, # 右边
                         relheight=1) # 下边

        self.scan_result()

        frame_right = ttk.LabelFrame(top, text="已经导入的POCEXP", bootstyle="success")
        frame_right.place(rely=0.1,# 上边
                          relwidth=0.2, # 右边
                          relheight=1.0) # 下边

        self.listdir()

        try:
            self.illustrate.edit_undo()  # 清空内容
        except:
            pass
        # 这个模块说明
        self.illustrate.insert(ttk.END,
                             '\n说明！GUI只是负责导入和清除不负责POCEXP的使用\n使用用命令行')


        # 显示线
        Import_pocxep_file = ttk.LabelFrame(top,
                                    text="导入POCEXP",
                                    bootstyle="success")
        Import_pocxep_file.place(relx=0.21,  # 左边
                         rely=0.1,  # 上边
                         relwidth=0.785,  # 右边
                         relheight=0.3)  # 下边

        # 密码字典
        ttk.Label(Import_pocxep_file,
                  text="导入POC/EXP",
                  bootstyle="success").grid(row=2,
                                            column=1,
                                            pady=20,
                                            padx=3) # 不设置w默认是在中间
        self.pocxep_file = tk.StringVar()
        ttk.Entry(Import_pocxep_file,
                   textvariable=self.pocxep_file,
                   bootstyle="success",
                   width=50).grid(row=2,
                                  column=2,
                                  pady=20,
                                  padx=3) # 不设置w默认是在中间

        # 选择文件
        Rad_Xray_many = tk.Button(Import_pocxep_file,
                                  text='选择文件',
                                  relief=tk.RAISED,
                                  command=self.PocAndExpScript_many,
                                  width=13)
        Rad_Xray_many.grid(row=2,
                          column=3,
                          pady=20,
                           padx=3)
        # 按钮开始
        label_1 = ttk.Button(Import_pocxep_file,
                             text="刷新添加POC/EXP",
                             bootstyle="success",
                             width=20,
                             command=self.Import_pocexp)
        label_1.grid(row=3,
                      column=1,
                      pady=20)
        # 按钮开始
        label_1 = ttk.Button(Import_pocxep_file,
                             text="清除POC/EXP",
                             bootstyle="success",
                             width=20,
                             command=self.purge_pocexp)
        label_1.grid(row=3,
                      column=2,
                      pady=20)

        # 按钮开始
        label_1 = ttk.Button(Import_pocxep_file,
                             text="查看导入的POC/EXP",
                             bootstyle="success",
                             width=20,
                             command=self.listdir)
        label_1.grid(row=3,
                      column=3,
                      pady=20)


        # information_gathering_frame_right = ttk.LabelFrame(top, text="暴力破解模块", bootstyle="success")
        # information_gathering_frame_right.place(rely=0.1,# 上边
        #                                       relwidth=0.2,
        #                                       relheight=1.0)



    # ---------------------导入POCEXP---------------------




    # ---------------------上面模块---------------------
    def Function(self):  # 上面模块
        # 显示模块
        Display_module = ttk.LabelFrame(top,
                                     text="模块",
                                     bootstyle="success")
        Display_module.place(relwidth=1,
                           relheight=0.1)

        # 界面上的信息收集
        Information_Collection = ttk.Button(Display_module,
                                    text='信息收集',  # 名字
                                    command=self.information_gathering,
                                    bootstyle="success",  # 样式
                                    width=22)
        Information_Collection.grid(row=1,
                                    column=1,
                                    padx=1,
                                    pady=1) # 用于控制外边距

        # 界面上的漏洞扫描
        Vulnerability_scanning = ttk.Button(Display_module,
                                            text='漏洞扫描',  # 名字
                                            command=self.VulnerabilityScan,
                                            bootstyle="success",  # 样式
                                            width=22)
        Vulnerability_scanning.grid(row=1,
                                column=2,
                                padx=1,
                                pady=1) # 用于控制外边距

        Brute_force_cracking=ttk.Button(Display_module,
                                        text='暴力破解',  # 名字
                                        command=self.Brute_force_module,
                                       bootstyle="success",  # 样式
                                       width=22)
        Brute_force_cracking.grid(row=1,
                                column=3,
                                padx=1,
                                pady=1) # 用于控制外边距
        POC_EXP=ttk.Button(Display_module,
                           command=self.PocAndExpScript,
                           text='导入POC/EXP',  # 名字
                           bootstyle="success",  # 样式
                           width=22)
        POC_EXP.grid(row=1,
                    column=4,
                    padx=1,
                    pady=1) # 用于控制外边距
        Encode=ttk.Button(Display_module, text='编码工具',  # 名字
                   command=self.Coding,
                   bootstyle="success",  # 样式
                   width=22)
        Encode.grid(row=1,
                    column=5,
                    padx=1,
                    pady=1) # 用于控制外边距
        Encode=ttk.Button(Display_module, text='实用工具',  # 名字
                   command=self.Utilities,
                   bootstyle="success",  # 样式
                   width=22)
        Encode.grid(row=1,
                    column=6,
                    padx=1,
                    pady=1) # 用于控制外边距
    # ---------------------上面模块---------------------

    # -------------------------扫描说明----------------------------------------
    def scan_result(self):

        scan_right = ttk.LabelFrame(top,
                                      text="说明",
                                      bootstyle="success")
        # relx = 0.25,  # 左边
        # rely = 0.3,  # 上边
        # relwidth = 0.7,  # 右边
        # relheight = 0.5)  # 下边

        scan_right.place(relx = 0.21,  # 左边
                           rely = 0.4,  # 上边
                           relwidth=0.78, # 右边
                           relheight=0.6) # 下边

        # --------------------------输出和滚动条----------------------------
        # 创建一个滚动条控件，默认为垂直方向
        output = ttk.Scrollbar(scan_right,
                               bootstyle="success")

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        output.pack(side=RIGHT,
                    fill=Y)

        # 设置文本框控件
        self.illustrate = ttk.Text(scan_right,
                                   yscrollcommand=output.set,  # 调用滚动条
                                   undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.illustrate.place(relwidth=0.99,
                              relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.illustrate.config(font=font1, foreground='#008B00')  # 颜色

        # for i in range(30):
        #     self.result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )
        self.illustrate.insert(tk.END,
                               f"""{'*' * 80}\n\n\n作者：w啥都学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        # 使用 command 关联控件的 yview、xview方法
        output.config(command=self.illustrate.yview)

    # -------------------------扫描输出结果----------------------------------------

    def main(self):
        self.Function()
        self.scan_result()


# 调用Tk()创建主窗口
top = ttk.Window(themename="darkly")

# top = ttk.Tk()
top.geometry('1250x680')

# 给主窗口起一个名字，也就是窗口的名字
top.title('Full-Scanner')
# 设置窗口的背景色为红色，也可以接受 16 进制的颜色值
# top.config(background="#2F4F4F")
# 添加程序的ico
icon = PhotoImage(file="avatar.ico")
top.tk.call('wm', 'iconphoto', top._w, icon)

# 创建对象
interface = interface()
interface.main()

top.mainloop()
#
# if __name__ == '__main__':
#     # 调用Tk()创建主窗口
#     top = ttk.Window()
#     # top = ttk.Tk()
#     top.geometry('1200x650')
#     # 给主窗口起一个名字，也就是窗口的名字
#     top.title('Full-Scanner')
#     # 设置窗口的背景色为红色，也可以接受 16 进制的颜色值
#     top.config(background="#2F4F4F")
#     # 添加程序的ico
#     icon = PhotoImage(file="/home/zss/图片/a8jt8-oqaex-001.ico")
#     top.tk.call('wm', 'iconphoto', top._w, icon)
#
#     # 创建对象
#     interface = interface()
#     interface.main()
#
#     top.mainloop()
