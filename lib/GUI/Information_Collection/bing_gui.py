# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件
from conf import config  # 配置文件





def bing_scanning(self,top):
    bing_top = tk.Tk()
    bing_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    bing_top.title('bing爬虫')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    bing_sbar = tk.Scrollbar(bing_top,
                             background="#00FA9A",
                             activebackground="#00FA9A",
                             troughcolor="#363636",
                             borderwidth=-2,
                             activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    bing_sbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # 设置文本框控件
    self.bing_result = ttk.Text(bing_top,
                                yscrollcommand=bing_sbar.set,  # 调用滚动条
                                undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.bing_result.place(relwidth=0.988,
                           relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.bing_result.config(font=font,
                            foreground='#008B00')  # 颜色

    bing_sbar.config(command=self.bing_result.yview)  # 设置鼠标可以
    # for i in range(30):
    #     self.bing_result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )

    try:
        self.bing_result.edit_undo()  # 清空内容
    except:
        pass

    from collect import bing
    # 定义线程对象a函数
    t = threading.Thread(target=bing.GUI,
                         args=(self.bing_url.get(),
                               self.bing_number.get(),
                               self.bing_result))
    # 启动线程
    t.start()

    bing_top.mainloop()


def bing_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass

    # 这个模块说明
    self.illustrate.insert(ttk.END,
                       '说明！\n搜索引擎爬虫、比如intitle:后台登陆 "学院"\n如果不指定默认就是100000')
    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="bing爬虫",
                                bootstyle="success")
    fofa_right.place(relx = 0.21,  # 左边
                     rely=0.1,# 上边
                     relwidth=0.785, # 右边
                     relheight=0.3) # 下边
    # 显示目标
    Display_the_target=ttk.Label(fofa_right,
                                 text="查询目标：",
                                 bootstyle="success")
    Display_the_target.grid(row=2,
                            column=1,
                            sticky=tk.W)

    # 输入目标
    # 生成动态字符串
    self.bing_url = tk.StringVar()
    Enter_the_target=ttk.Entry(fofa_right,
                               textvariable=self.bing_url,
                               bootstyle="success",
                               width=30)
    Enter_the_target.grid(row=2,
                          column=2,
                          sticky=tk.W)

    # 显示可选参数
    ttk.Label(fofa_right, text="可选参数：如果不指定默认就是100000",
              bootstyle="success").grid(row=3,
                                        column=1,
                                        sticky=tk.W)

    # 显示设置延迟指定页数
    ttk.Label(fofa_right,
              text="指定页数：",
              bootstyle="success").grid(row=4,
                                        column=1,
                                        sticky=tk.W)
    # 设置指定页数
    # 生成动态字符串
    self.bing_number = tk.StringVar()
    bing_n = ttk.Entry(fofa_right,
                       textvariable=self.bing_number,
                       bootstyle="success",
                       width=15)
    bing_n.grid(row=4, column=2, sticky=tk.W)
    bing_n.insert(0, 100000) # 默认值

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.bing_scanning)
    label_1.grid(row=2, column=5, padx=30)  # 位置