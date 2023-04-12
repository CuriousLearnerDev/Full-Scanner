# -*- coding:utf-8 -*-
import tkinter as tk
from PIL.ImageTk import PhotoImage
import ttkbootstrap as ttk

# # 调用Tk()创建主窗口
# top = ttk.Window()
# # top = ttk.Tk()
# top.geometry('1200x650')
# # 给主窗口起一个名字，也就是窗口的名字
# top.title('Full-Scanner')
# # 设置窗口的背景色为红色，也可以接受 16 进制的颜色值
# top.config(background="#1C1C1C")
# # 添加程序的ico
# icon = PhotoImage(file="/home/zss/图片/a8jt8-oqaex-001.ico")
# top.tk.call('wm', 'iconphoto', top._w, icon)
#
# # ------------------------功能-----------------------------------------
#
#
#
#
# def fofa_scanning(Fofa_url):
#     print(Fofa_url.get())
#
# def fofa_passive_information_gathering():
#
#     # 显示线
#     fofa_right = ttk.LabelFrame(top, text="fofa模块", bootstyle="secondary")
#     fofa_right.place(x=270,  # 左右
#                   y=60,  # 上下
#                   relwidth=0.78,
#                   relheight=0.23)
#
#     # 显示目标
#     ttk.Label(fofa_right, text="目标：", bootstyle="success").grid(row=2, column=1)
#
#     # 输入目标
#     # 生成动态字符串
#
#     Fofa_url = ttk.StringVar()
#     ttk.Entry(fofa_right,textvariable=Fofa_url, bootstyle="success",width=30).grid(row=2, column=2)
#
#     # 显示Cookie
#     ttk.Label(fofa_right, text=" Cookie值：", bootstyle="success").grid(row=2, column=3)
#
#     # Cookie
#     # 生成动态字符串
#     Fofa_Cookie = ttk.StringVar()
#     ttk.Entry(fofa_right,textvariable=Fofa_Cookie, bootstyle="success",width=30).grid(row=2, column=4)
#
#     # 显示可选参数
#     ttk.Label(fofa_right, text="可选参数：", bootstyle="success").grid(row=3, column=1)
#
#     # 显示设置延迟时间
#     ttk.Label(fofa_right, text="设置延迟时间：", bootstyle="success").grid(row=4, column=1)
#
#     # 设置延迟时间
#     ttk.Entry(fofa_right, bootstyle="success",width=30).grid(row=4, column=2)
#
#     # # 创建下拉菜单
#     # cbox = ttk.Combobox(fofa_right,bootstyle="success",width=30)
#     #
#     # # 设置下拉菜单中的值
#     # cbox['value'] = ('CVE-2022-26134', 'CVE-2022-26134', 'php')
#     # # 通过 current() 设置下拉菜单选项的默认值
#     # ttk.Label(fofa_right, text="调用：", bootstyle="success").grid(row=4, column=3)
#     #
#     # cbox.current(2)
#     # cbox.grid(row=4, column=4)
#
#     # 按钮开始
#     label_1 = ttk.Button(fofa_right,
#                          text="开始",
#                          bootstyle="success-outline",
#                          width=13,
#                          command=lambda: fofa_scanning(Fofa_url))
#     label_1.grid(row=2,column=5) # 位置
#
# # 设置回调函数
# def passive_information_gathering():
#     frame_right = ttk.LabelFrame(top, text="信息收集模块", bootstyle="secondary")
#     frame_right.place(x=5,  # 左右
#                       y=60,  # 上下
#                       relwidth=0.2,
#                       relheight=1.0)
#
#     label_1 = ttk.Button(frame_right,
#                          text="fofa搜索结果提取",
#                          bootstyle="success-outline",
#                          width=22,
#                          command=fofa_passive_information_gathering)
#
#     label_1.grid(row=1,column=1) # 位置
#     label_1 = ttk.Button(frame_right,
#                          text="shodan信息收集",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=2,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="whois查询",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=3,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="bing搜索引擎爬虫",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=4,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="google搜索引擎爬虫",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=5,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="子域名查询",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=6,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="目标cms识别",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=7,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="备份文件扫描",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=8,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="后台扫描",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=7,column=1) # 位置
#
#     label_1 = ttk.Button(frame_right,
#                          text="端口扫描",
#                          bootstyle="success-outline",
#                          width=22)
#     label_1.grid(row=7,column=1) # 位置
#
#
# def callback():
#     pass
#
# #生成动态字符串
# passive_information_gathering_dstr = tk.StringVar()
#
# ttk.Button(top,text='信息收集', # 名字
#          bootstyle="success", # 样式
#          width=20,command=passive_information_gathering).place(x=5, # 左右
#                                                         y=20) # 上下
#
# ttk.Button(top,text='漏洞扫描', # 名字
#          bootstyle="success", # 样式
#          width=20,command=callback).place(x=210, # 左右
#                                     y=20) # 上下
#
# ttk.Button(top,text='暴力破解', # 名字
#          bootstyle="success", # 样式
#          width=20,command=callback).place(x=415, # 左右
#                                     y=20) # 上下
#
#
# ttk.Button(top,text='导入POC/EXP', # 名字
#          bootstyle="success", # 样式
#          width=20,command=callback).place(x=620, # 左右
#                                     y=20) # 上下
# # -------------------------模块----------------------------------------
#
# frame_right = ttk.LabelFrame(top, text="模块", bootstyle="secondary")
# frame_right.place(x=5,  # 左右
#                   y=60,  # 上下
#                   relwidth=0.2,
#                   relheight=1.0)
#
# # -------------------------扫描结果----------------------------------------
# frame_right2 = ttk.LabelFrame(top,
#                              text="结果",
#                              bootstyle="secondary")
#
# frame_right2.place(x=270,  # 左右
#                   y=220,  # 上下
#                   relwidth=1.0,
#                   relheight=1.0)
#
# # --------------------------输出和滚动条----------------------------
# # 创建一个滚动条控件，默认为垂直方向
# sbar1= ttk.Scrollbar(top)
#
# # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
# sbar1.place(x=1190,
#             y=220,
#             relheight=0.65)
#
# # 设置文本框控件
# text = tk.Text(frame_right2,yscrollcommand = sbar1.set,insertbackground='#00FA9A')
# # 在主窗口内显示
# text.place(relwidth=0.76,
#           relheight=0.68)
#
# # for i in range(30):
# #     text.insert(tk.END,'第'+ str(i+1)+'次\n' )
# # 使用 command 关联控件的 yview、xview方法
# text.insert(tk.END,'第次\n' )
# sbar1.config(command =text.yview)
#
# text.edit_undo()
#
# # -----------------------------------------------------------------
# top.mainloop()


whois_top = ttk.Window(themename="darkly")
# top = ttk.Tk()
whois_top.geometry('780x800+2000+100')
# 给主窗口起一个名字，也就是窗口的名字
whois_top.title('whois')


# 创建一个滚动条控件，默认为垂直方向
whois_sbar= ttk.Scrollbar(whois_top,
                      bootstyle="success")

# 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
whois_sbar.pack(side=tk.RIGHT,
                 fill=tk.Y)


# 设置文本框控件
result = ttk.Text(whois_top,
                   yscrollcommand=whois_sbar.set,  # 调用滚动条
                   undo=True)  # 开启删除内容
# 在主窗口内显示
result.place(relwidth=0.98,
            relheight=1.0)
#
# for i in range(30):
#     result.insert(tk.END,'第123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789'+ str(i+1)+'次\n' )
#
#
# whois_sbar.config(command=result.yview) # 设置鼠标可以


whois_top.mainloop()




