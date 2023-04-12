# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件



def port_scanning(self):
    port_top = tk.Tk()
    port_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    port_top.title('端口扫描')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    sbar = tk.Scrollbar(port_top,
                        background="#00FA9A",
                        activebackground="#00FA9A",
                        troughcolor="#363636",
                        borderwidth=-2,
                        activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    sbar.pack(side=tk.RIGHT,
              fill=tk.Y)

    # 设置文本框控件
    self.port_result = tk.Text(port_top,
                               yscrollcommand=sbar.set,  # 调用滚动条
                               undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.port_result.place(relwidth=0.988,
                           relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.port_result.config(font=font, foreground='#008B00')  # 颜色

    sbar.config(command=self.port_result.yview)  # 设置鼠标可以

    # -----------------------------进度条-----------------------------
    port_progressbar = ttk.Progressbar(port_top)
    port_progressbar.pack(side=tk.BOTTOM, fill=tk.X)

    # # 进度值最大值
    # port_progressbar['maximum'] = 50
    # # 进度值初始值
    # port_progressbar['value'] = 0
    # for i in range(50):
    #     time.sleep(0.5)
    #     port_progressbar['value'] += 10

    # --------------------------------------------------------------

    # for i in range(30):
    #     self.port_result.insert(tk.END,
    #                              '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
    #                                  i + 1) + '次\n')
    # try:
    #     self.port_result.edit_undo()  # 清空内容
    # except:
    #     pass
    from Initiative.portscan import port
    # 定义线程 预防卡
    t = threading.Thread(target=port.GUI,
                         args=(self.port_ip.get(),
                               self.port_p.get(),
                               self.port_t.get(),
                               self.port_result,
                               port_progressbar))
    # 启动线程
    t.start()

    port_top.mainloop()


def port_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n指定端口、不指定默认常见的端口\n指定比如：1-65535或者22,80,3306\n不指定线程默认：1\n线程太多会出问题')

    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="端口扫描",
                                bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边
    # 显示设置代理
    ttk.Label(fofa_right,
              text="目标IP/域名：",
              bootstyle="success").grid(row=3,
                                        column=1,
                                        sticky=tk.W,
                                        padx=25)
    # 设置指定页数
    # 生成动态字符串
    self.port_ip = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.port_ip,
              bootstyle="success",
              width=30).grid(row=3,
                             column=2,
                             sticky=tk.W)

    # 显示
    ttk.Label(fofa_right, text=" 扫描的端口：", bootstyle="success").grid(row=3, column=3, sticky=tk.W)
    # 指定页数
    # 生成动态字符串
    self.port_p = tk.StringVar()
    ttk.Entry(fofa_right, textvariable=self.port_p, bootstyle="success", width=10).grid(row=3, column=4, sticky=tk.W)

    # 显示
    ttk.Label(fofa_right, text=" 线程数：", bootstyle="success").grid(row=4, column=1, sticky=tk.W, padx=25)
    # 指定页数
    # 生成动态字符串
    self.port_t = tk.StringVar()
    port_t_default = ttk.Entry(fofa_right,
                               textvariable=self.port_t,
                               bootstyle="success",
                               width=10)
    port_t_default.grid(row=4,
                        column=2,
                        sticky=tk.W,
                        pady=25)
    port_t_default.insert(0, 1)  # 默认值
    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.port_scanning)
    label_1.grid(row=3, column=5, padx=50)  # 位置


