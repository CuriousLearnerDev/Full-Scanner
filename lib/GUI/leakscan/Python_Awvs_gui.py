# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
from conf import config  # 配置文件


def Python_Awvs_scanning(self):
    Python_Awvs_top = tk.Tk()
    Python_Awvs_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    Python_Awvs_top.title('Py调用AWVS联动Xray联动钉钉推送')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    fofa_sbar = tk.Scrollbar(Python_Awvs_top,
                             background="#00FA9A",
                             activebackground="#00FA9A",
                             troughcolor="#363636",
                             borderwidth=-2,
                             activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    fofa_sbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # 设置文本框控件
    self.awvs_xray_dd_result = ttk.Text(Python_Awvs_top,
                                        yscrollcommand=fofa_sbar.set,  # 调用滚动条
                                        undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.awvs_xray_dd_result.place(relwidth=0.988,
                                   relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.awvs_xray_dd_result.config(font=font,
                                    foreground='#008B00')  # 颜色

    fofa_sbar.config(command=self.awvs_xray_dd_result.yview)  # 设置鼠标可以
    # for i in range(30):
    #     self.fofa_result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )

    try:
        self.awvs_xray_dd_result.edit_undo()  # 清空内容
    except:
        pass
    from leakscan.awvs import python_awvs
    # self.Python_Awvs_result.insert(tk.END,self.awvs_xray_dd_cbox.get())
    # python_awvs.main_xray_dd()
    t = threading.Thread(target=python_awvs.main_xray_dd, args=(self.awvs_xray_dd_url.get(),
                                                                self.awvs_xray_dd_ApiKey.get(),
                                                                self.awvs_xray_dd_file.get(),
                                                                self.awvs_xray_dd_cbox.get(),
                                                                self.awvs_xray_dd_Time.get(),
                                                                self.awvs_xray_dd_name.get(),
                                                                self.awvs_xray_dd_Broker.get(),
                                                                self.awvs_xray_dd_ddapi.get(),
                                                                self.awvs_xray_dd_result))
    # 启动线程
    t.start()

    Python_Awvs_top.mainloop()

def Python_Awvs(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '\n\n说明！\nPy调用AWVS联动Xray联动钉钉推送\n速度说明：slow(慢)、moderate(中)、fasts(快)\n联动Xray扫描可以直接把代理设置成Xray的\n钉钉推送的token，不想每次都添加可以去config配置文件里面添加')

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
    self.awvs_xray_dd_url = tk.StringVar()
    Awvs_Host = ttk.Entry(fofa_right, textvariable=self.awvs_xray_dd_url, bootstyle="success", width=30)
    Awvs_Host.grid(row=2, column=2, sticky=tk.W)
    Awvs_Host.insert(0, 'https://127.0.0.1:3443')

    # 指定线程
    ttk.Label(fofa_right,
              text=" 扫描备注：",
              bootstyle="success").grid(row=2, column=3, sticky=tk.W)
    # 扫描备注
    # 生成动态字符串
    self.awvs_xray_dd_name = tk.StringVar()
    Awvs_Name = ttk.Entry(fofa_right, textvariable=self.awvs_xray_dd_name, bootstyle="success", width=20)
    Awvs_Name.grid(row=2, column=4, sticky=tk.W)
    Awvs_Name.insert(0, 'Full-Scanner')

    # awvs的ApiKey
    ttk.Label(fofa_right,
              text="ApiKey：",
              bootstyle="success").grid(row=4, column=1, sticky=tk.W)
    # 指定awvs的ApiKey
    # 生成动态字符串
    self.awvs_xray_dd_ApiKey = tk.StringVar()
    awvs_xray_dd_ApiKey=ttk.Entry(fofa_right,
              textvariable=self.awvs_xray_dd_ApiKey,
              bootstyle="success",
              width=30)
    awvs_xray_dd_ApiKey.grid(row=4, column=2, sticky=tk.W)
    awvs_xray_dd_ApiKey.insert(0,config.SeriousConfig['awvs'])


    # 指定文件批量扫描
    ttk.Label(fofa_right,
              text="批量扫描文件：",
              bootstyle="success").grid(row=4, column=3, sticky=tk.W)
    # 指定文件批量扫描
    # 生成动态字符串
    self.awvs_xray_dd_file = tk.StringVar()
    Awvs_back_dictionary = ttk.Entry(fofa_right, textvariable=self.awvs_xray_dd_file, bootstyle="success", width=30)
    Awvs_back_dictionary.grid(row=4, column=4, sticky=tk.W)

    # 选择文件
    Backupfilescan_document = tk.Button(fofa_right,
                                        text='选择文件',
                                        relief=tk.RAISED,
                                        command=self.Python_Awvs_many)
    Backupfilescan_document.grid(row=4,
                                 column=5,
                                 sticky=tk.W)

    # 推送钉钉API
    ttk.Label(fofa_right,
              text="推送钉钉API：",
              bootstyle="success").grid(row=5, column=1, sticky=tk.W)

    # 推送钉钉API
    self.awvs_xray_dd_ddapi = tk.StringVar()
    Python_Awvs_dd=ttk.Entry(fofa_right,
              textvariable=self.awvs_xray_dd_ddapi,
              bootstyle="success",
              width=30)
    Python_Awvs_dd.grid(row=5, column=2, sticky=tk.W)
    Python_Awvs_dd.insert(0,config.SeriousConfig['dingtalk'])

    # ttk.Label(fofa_right,
    #           text="",
    #           bootstyle="success").grid(row=5, column=3, sticky=tk.W)

    # 多少秒添加
    ttk.Label(fofa_right,
              text="多少秒添加：",
              bootstyle="success").grid(row=5, column=3, sticky=tk.W)

    # 多少秒添加
    self.awvs_xray_dd_Time = tk.StringVar()
    Awvs_Time = ttk.Entry(fofa_right,
                          textvariable=self.awvs_xray_dd_Time,
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
    ttk.Label(fofa_right,
              text="代理IP(可以是Xray)：",
              bootstyle="success").grid(row=6, column=1, sticky=tk.W)

    # 显示设置代理
    self.awvs_xray_dd_Broker = tk.StringVar()
    Awvs_Broker = ttk.Entry(fofa_right,
                            textvariable=self.awvs_xray_dd_Broker,
                            bootstyle="success",
                            width=30)
    Awvs_Broker.grid(row=6, column=2, sticky=tk.W)
    Awvs_Broker.insert(0, "127.0.0.1:7777")

    # 扫描速度设置
    ttk.Label(fofa_right,
              text="扫描速度设置：",
              bootstyle="success").grid(row=6, column=3, sticky=tk.W)
    # 扫描速度设置
    self.awvs_xray_dd_cbox = ttk.Combobox(fofa_right, width=10)
    # 设置下拉菜单中的值
    self.awvs_xray_dd_cbox['value'] = ('slow', 'moderate', 'fasts')

    # 通过 current() 设置下拉菜单选项的默认值
    self.awvs_xray_dd_cbox.current(1)
    # 绑定下拉菜单事件
    self.awvs_xray_dd_cbox.bind("<<ComboboxSelected>>")
    self.awvs_xray_dd_cbox.grid(row=6, column=4, sticky=tk.W)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.Python_Awvs_scanning)
    label_1.grid(row=2, column=5)  # 位置
