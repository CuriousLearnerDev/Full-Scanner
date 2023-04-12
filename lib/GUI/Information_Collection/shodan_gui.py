# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件
from conf import config  # 配置文件


def shodan_scanning(self):
    result_top = tk.Tk()
    result_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    result_top.title('shodan查询')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    sbar = tk.Scrollbar(result_top,
                        background="#00FA9A",
                        activebackground="#00FA9A",
                        troughcolor="#363636",
                        borderwidth=-2,
                        activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    sbar.pack(side=tk.RIGHT,
              fill=tk.Y)

    # 设置文本框控件
    self.shodan_result = ttk.Text(result_top,
                                  yscrollcommand=sbar.set,  # 调用滚动条
                                  undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.shodan_result.place(relwidth=0.988,
                             relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.shodan_result.config(font=font, foreground='#008B00')  # 颜色

    sbar.config(command=self.shodan_result.yview)  # 设置鼠标可以

    try:
        self.shodan_result.edit_undo()  # 清空内容
    except:
        pass
    from collect import shodan
    # 定义线程 预防卡
    t = threading.Thread(target=shodan.GUI,
                         args=(self.shodan_ip.get(),
                               self.shodan_api.get(),
                               self.shodan_result,))
    # 启动线程
    t.start()

    result_top.mainloop()

def shodan_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n用-API参数指定\n如果不想每次都指定可以去config.py文件里面添加')

    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="shodan查询",
                                bootstyle="success")
    fofa_right.place(relx = 0.21,  # 左边
                     rely=0.1,# 上边
                     relwidth=0.785, # 右边
                     relheight=0.3) # 下边
    # 显示目标
    ttk.Label(fofa_right,
              text="查询目标IP(普通用户只能用IP)：",
              bootstyle="success").grid(row=2,
                                        column=1,
                                        sticky=tk.W)

    # 输入目标
    # 生成动态字符串
    self.shodan_ip = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.shodan_ip,
              bootstyle="success",
              width=30).grid(row=2,
                             column=2,
                             sticky=tk.W)

    # 指定API的密钥
    ttk.Label(fofa_right,
              text="API的密钥(不想每次添加可以去config.py文件添加)：",
              bootstyle="success").grid(row=4,
                                        column=1,
                                        sticky=tk.W)
    # 指定API的密钥
    self.shodan_api = tk.StringVar()
    Shodan_api=ttk.Entry(fofa_right,
              textvariable=self.shodan_api,
              bootstyle="success", width=30)
    Shodan_api.grid(row=4,
                  column=2,
                  sticky=tk.W, pady=25)


    Shodan_api.insert(0,config.SeriousConfig['shodan'])
    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.shodan_scanning)
    label_1.grid(row=2, column=5, padx=50)  # 位置