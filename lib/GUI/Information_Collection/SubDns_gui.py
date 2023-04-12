# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件


def SubDns_scanning(self):
    SubDns_top = tk.Tk()
    SubDns_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    SubDns_top.title('子域名探测')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    SubDns_sbar = tk.Scrollbar(SubDns_top,
                               background="#00FA9A",
                               activebackground="#00FA9A",
                               troughcolor="#363636",
                               borderwidth=-2,
                               activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    SubDns_sbar.pack(side=tk.RIGHT,
                     fill=tk.Y)

    # 设置文本框控件
    self.SubDns_result = ttk.Text(SubDns_top,
                                  yscrollcommand=SubDns_sbar.set,  # 调用滚动条
                                  undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.SubDns_result.place(relwidth=0.988,
                             relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.SubDns_result.config(font=font, foreground='#008B00')  # 颜色

    SubDns_sbar.config(command=self.SubDns_result.yview)  # 设置鼠标可以

    # for i in range(30):
    #     self.SubDns_result.insert(tk.END,
    #                              '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
    #                                  i + 1) + '次\n')
    try:
        self.SubDns_result.edit_undo()  # 清空内容
    except:
        pass
    from collect.SubDnsDetect import SubDns

    # 定义线程 预防卡
    t = threading.Thread(target=SubDns.GUI, args=(self.Sub_dns.get(), self.SubDns_result,))
    # 启动线程
    t.start()

    SubDns_top.mainloop()


def SubDns_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n这个子域名探测采用的一些搜索引擎进行域名探测有bing、crtsh、fofa、censys等\n不需要输入API这个是采集的查询结果的页面进行提取的\n注意:访问国外网站可能会出现访问不了的情况！')
    # 显示线
    fofa_right = ttk.LabelFrame(top, text="子域名探测", bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边
    # 显示目标
    ttk.Label(fofa_right, text="目标DNS：", bootstyle="success").grid(row=2, column=1, sticky=tk.W, padx=40)

    # 输入目标
    # 生成动态字符串
    self.Sub_dns = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.Sub_dns, bootstyle="success", width=30).grid(row=2, column=2, sticky=tk.W,
                                                                                         pady=40)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.SubDns_scanning)
    label_1.grid(row=2, column=5, padx=50)  # 位置

