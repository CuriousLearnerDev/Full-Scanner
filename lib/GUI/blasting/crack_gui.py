# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import threading  # 预防卡住

def crack_scanning(self):
    whois_top = tk.Tk()
    whois_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    whois_top.title('web登录破解')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    whois_sbar = tk.Scrollbar(whois_top,
                              background="#00FA9A",
                              activebackground="#00FA9A",
                              troughcolor="#363636",
                              borderwidth=-2,
                              activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    whois_sbar.pack(side=tk.RIGHT,
                    fill=tk.Y)

    # 设置文本框控件
    self.crack_result = ttk.Text(whois_top,
                                 yscrollcommand=whois_sbar.set,  # 调用滚动条
                                 undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.crack_result.place(relwidth=0.988,
                            relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.crack_result.config(font=font,
                             foreground='#008B00')  # 颜色

    whois_sbar.config(command=self.crack_result.yview)  # 设置鼠标可以

    try:
        self.crack_result.edit_undo()  # 清空内容
    except:
        pass

    # for i in range(30):
    #     self.whois_result.insert(tk.END,
    #                              '第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789' + str(
    #                                  i + 1) + '次\n')
    from thirdparty.extracted import webcrack

    # 定义线程 预防卡
    t = threading.Thread(target=webcrack.gui,
                         args=(self.crack_url.get(),
                               self.crack_result,))
    # 启动线程
    t.start()

    whois_top.mainloop()
def crack(self,top):

    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass

    # 这个模块说明
    self.illustrate.insert(ttk.END,
                           '说明！\n web登录破解\n这个不是本作者而写是用的这个地址的：https://github.com/yzddmr6/WebCrack\n 做了一些修改')

    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="web登录破解",
                                bootstyle="success")
    fofa_right.place(relx=0.21,  # 左边
                     rely=0.1,  # 上边
                     relwidth=0.785,  # 右边
                     relheight=0.3)  # 下边

    # 显示目标
    ttk.Label(fofa_right,
              text="web登录url地址：",
              bootstyle="success").grid(row=2,
                                        column=1,
                                        sticky=tk.W,
                                        padx=40)

    # 输入目标
    # 生成动态字符串
    self.crack_url = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.crack_url,
              bootstyle="success",
              width=30).grid(row=2,
                             column=2,
                             sticky=tk.W, pady=40)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.crack_scanning)
    label_1.grid(row=2, column=5, padx=50)  # 位置