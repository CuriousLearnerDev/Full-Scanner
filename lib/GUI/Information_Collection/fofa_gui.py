# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
import tkinter.font as tf
import threading  # 预防卡住
import sys
sys.path.append("../../") # 解决上级库文件
from conf import config  # 配置文件


def fofa_scanning(self,top):
    fofa_top = tk.Tk()
    fofa_top.geometry('780x800')
    # 给主窗口起一个名字，也就是窗口的名字
    fofa_top.title('FOFA')
    # whois_top.config(background="#2F4F4F")

    # 创建一个滚动条控件，默认为垂直方向
    fofa_sbar = tk.Scrollbar(fofa_top,
                             background="#00FA9A",
                             activebackground="#00FA9A",
                             troughcolor="#363636",
                             borderwidth=-2,
                             activerelief='groove')

    # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
    fofa_sbar.pack(side=tk.RIGHT,
                   fill=tk.Y)

    # 设置文本框控件
    self.fofa_result = ttk.Text(fofa_top,
                                yscrollcommand=fofa_sbar.set,  # 调用滚动条
                                undo=True)  # 开启删除内容
    # 在主窗口内显示
    self.fofa_result.place(relwidth=0.988,
                           relheight=1.0)

    # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
    font = tk.font.Font()
    self.fofa_result.config(font=font,
                            foreground='#008B00')  # 颜色

    fofa_sbar.config(command=self.fofa_result.yview)  # 设置鼠标可以
    # for i in range(30):
    #     self.fofa_result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )

    try:
        self.fofa_result.edit_undo()  # 清空内容
    except:
        pass

    from collect import fofa_api

    print()

    # 定义线程对象a函数
    t = threading.Thread(target=fofa_api.GUI,
                         args=(self.Fofa_api_url.get(),
                               self.Fofa_api_key.get(),
                               self.Fofa_api_email.get(),
                               self.Fofa_api_size.get(),
                               self.fofa_result))
    # 启动线程
    t.start()

    fofa_top.mainloop()

def fofa_passive_information_gathering(self,top):
    try:
        self.illustrate.edit_undo()  # 清空内容
    except:
        pass
    # 这个模块说明
    self.illustrate.insert(ttk.END,
                       '\n\n说明！\nkey值和email邮箱\n如果不想每次都指定可以去config.py文件里面添加key值和email邮箱')


    # 显示线
    fofa_right = ttk.LabelFrame(top,
                                text="fofa模块",
                                bootstyle="success")
    fofa_right.place(relx = 0.21,  # 左边
                     rely=0.1,# 上边
                     relwidth=0.785, # 右边
                     relheight=0.3) # 下边
    # 显示目标
    ttk.Label(fofa_right, text="搜索内容：",
              bootstyle="success").grid(row=2,
                                        column=1,
                                        sticky=tk.W)

    # 输入目标
    # 生成动态字符串

    self.Fofa_api_url = tk.StringVar()
    ttk.Entry(fofa_right,
              textvariable=self.Fofa_api_url,
              bootstyle="success",
              width=40).grid(row=2,
                             column=2,
                             sticky=tk.W)

    # 查询数量
    ttk.Label(fofa_right,
              text="查询数量",
              bootstyle="success").grid(row=4,
                                        column=1,
                                        sticky=tk.W)

    # 设置查询数量
    self.Fofa_api_size = tk.StringVar()
    Fofa_n=ttk.Entry(fofa_right,
                     textvariable=self.Fofa_api_size,
                     bootstyle="success",
                     width=15)
    Fofa_n.grid(row=4,
                column=2,
                sticky="w")
    Fofa_n.insert(0, 10000)  # 默认值



    ttk.Label(fofa_right,
              text=" key值：",
              bootstyle="success").grid(row=5,
                                        column=1,
                                        sticky=tk.W)
    # key
    # 生成动态字符串
    self.Fofa_api_key = tk.StringVar()
    Fofa_key=ttk.Entry(fofa_right,
              textvariable=self.Fofa_api_key,
              bootstyle="success",
              width=30)
    Fofa_key.grid(row=5,
                 column=2,
                 sticky=tk.W)
    Fofa_key.insert(0,config.SeriousConfig['fofa_api']['key'])

    ttk.Label(fofa_right,
              text=" email邮箱：",
              bootstyle="success").grid(row=6,
                                        column=1,
                                        sticky=tk.W)
    # email邮箱
    # 生成动态字符串
    self.Fofa_api_email = tk.StringVar()
    Fofa_email=ttk.Entry(fofa_right,
              textvariable=self.Fofa_api_email,
              bootstyle="success",
              width=30)
    Fofa_email.grid(row=6,
                    column=2,
                    sticky=tk.W)
    Fofa_email.insert(0, config.SeriousConfig['fofa_api']['email'])  # 默认值


    # 创建下拉菜单
    #cbox = ttk.Combobox(fofa_right, bootstyle="success", width=20)

    # # 设置下拉菜单中的值
    # cbox['value'] = ('无', 'CVE-2022-26134', '')
    # # 通过 current() 设置下拉菜单选项的默认值
    # cbox.current(0)
    #
    # ttk.Label(fofa_right, text="调用：", bootstyle="success").grid(row=4, column=3, sticky=tk.W)
    #
    # cbox.grid(row=4, column=4)

    # 按钮开始
    label_1 = ttk.Button(fofa_right,
                         text="开始",
                         bootstyle="success",
                         width=13,
                         command=self.fofa_scanning)
    label_1.grid(row=2,
                 column=5,
                 padx=20)  # 位置