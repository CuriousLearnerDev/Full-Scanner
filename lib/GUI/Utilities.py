
# -*- coding:utf-8 -*-
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import RIGHT
import threading  # 预防卡住
import re
import time
import urllib.parse



class tool:
    # ---------------------删除重复的---------------------

    def Remove_duplicates_threading(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = result.split("\n")  # 遇见回车就
        #print(result)
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        try:
            self.Process_Get.edit_undo()  # 清空内容
        except:
            pass
        for w in result:
            fi2 = self.Output_the_result.get("1.0","end") # 获取输入的内容
            txt2 = fi2.split("\n")  # 遇见回车就

            if w not in txt2:	#如果从源文档中读取的内容不在目标文档中则写入，否则跳过，实现去除重复功能！
                self.Output_the_result.insert(tk.END, w + "\n")  # 叫编码结果输出出来
                self.Output_the_result.see(tk.END)  # 始终处于最底端
            else:
                self.Process_Get.insert(tk.END, "内容重复的有："+w + "\n")  # 叫编码结果输出出来
                self.Process_Get.see(tk.END)  # 始终处于最底端

        self.Process_Get.insert(tk.END, "完成！\n")  # 叫编码结果输出出来
        self.Process_Get.see(tk.END)  # 始终处于最底端
    def Remove_duplicates(self):
        def start():
            # 定义线程对象a函数
            t = threading.Thread(target=self.Remove_duplicates_threading)
            # 启动线程
            t.start()
        self.Input_box()
        self.Output_box()
        self.Process_box()

        label_1 = ttk.Button(self.Input_right,
                             text="开始",
                             bootstyle="success",
                             command=start,
                             width=20,)
        label_1.grid(row=0,
                    column=1,
                    sticky=tk.W)

        ttk.Label(self.Input_right,
                  text="说明：删除重复的内容留一个",
                  bootstyle="success").grid(row=0,
                                            column=2,
                                            sticky=tk.W)
    # ---------------------删除重复的---------------------
    # ---------------------删除文件里面空白---------------------

    def Delete_the_blank_threading(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = result.split("\n")  # 遇见回车就
        #print(result)
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        try:
            self.Process_Get.edit_undo()  # 清空内容
        except:
            pass


        self.Process_Get.insert(tk.END, "正在过滤！\n")
        for i in result:
            if (i.strip()) != '':
                self.Output_the_result.insert(tk.END, i.strip()+"\n")  # 叫编码结果输出出来
                self.Output_the_result.see(tk.END)  # 始终处于最底端

        self.Process_Get.insert(tk.END, "完成！\n")  # 叫编码结果输出出来

    def Delete_the_blank(self):
        def start():
            # 定义线程对象a函数
            t = threading.Thread(target=self.Delete_the_blank_threading)
            # 启动线程
            t.start()


        self.Input_box()
        self.Output_box()
        self.Process_box()
        label_1 = ttk.Button(self.Input_right,
                             text="开始",
                             bootstyle="success",
                             command=start,
                             width=20,)
        label_1.grid(row=0,
                    column=1,
                    sticky=tk.W)

        ttk.Label(self.Input_right,
                  text="说明：删除空行的",
                  bootstyle="success").grid(row=0,
                                            column=2,
                                            sticky=tk.W)
    # ---------------------删除文件里面空白---------------------
    # ---------------------URL分割域名(不http://)---------------------
            # 光提取文件中的域名/IP、比如文件有一个http://1.1.1.1/x/x/x/x、提取出来的就是1.1.1.1
    def Interface_dns_threading(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = result.split("\n")  # 遇见回车就
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        try:
            self.Process_Get.edit_undo()  # 清空内容
        except:
            pass

        self.Process_Get.insert(tk.END, "正在提取！\n")
        for dns in result:
            domian = urllib.parse.urlparse(dns).netloc
            if not domian == '':
                self.Output_the_result.insert(tk.END, domian+"\n")  # 叫编码结果输出出来
                self.Output_the_result.see(tk.END)  # 始终处于最底端

        self.Process_Get.insert(tk.END, "完成！\n")  # 叫编码结果输出出来

    def Interface_dns(self):
        def start():
            # 定义线程对象a函数
            t = threading.Thread(target=self.Interface_dns_threading)
            # 启动线程
            t.start()


        self.Input_box()
        self.Output_box()
        self.Process_box()
        label_1 = ttk.Button(self.Input_right,
                             text="开始",
                             bootstyle="success",
                             command=start,
                             width=20,)
        label_1.grid(row=0,
                    column=1,
                    sticky=tk.W)

        ttk.Label(self.Input_right,
                  text="说明：http://1.1.1.1/x/x提取出来的就是1.1.1.1",
                  bootstyle="success").grid(row=0,
                                            column=2,
                                            sticky=tk.W)

    # ---------------------URL分割域名(不http://)---------------------

    # ---------------------URL分割域名(带http://)---------------------

    def Interface_http_threading(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = result.split("\n")  # 遇见回车就
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        try:
            self.Process_Get.edit_undo()  # 清空内容
        except:
            pass

        self.Process_Get.insert(tk.END, "正在提取！\n")
        for dns in result:
            a = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{6}))+', dns)
            for i in a:
                self.Output_the_result.insert(tk.END, i + "\n")  # 叫编码结果输出出来
                self.Output_the_result.see(tk.END)  # 始终处于最底端

        self.Process_Get.insert(tk.END, "完成！\n")  # 叫编码结果输出出来

    def Interface_http(self):
        def start():
            # 定义线程对象a函数
            t = threading.Thread(target=self.Interface_http_threading)
            # 启动线程
            t.start()

        self.Input_box()
        self.Output_box()
        self.Process_box()

        label_1 = ttk.Button(self.Input_right,
                             text="开始",
                             bootstyle="success",
                             command=start,
                             width=20,)
        label_1.grid(row=0,
                    column=1,
                    sticky=tk.W)

        ttk.Label(self.Input_right,
                  text="说明：http://1.1.1.1/x/x提取出来的就是http://1.1.1.1",
                  bootstyle="success").grid(row=0,
                                            column=2,
                                            sticky=tk.W)
    # ---------------------URL分割域名(带http://)---------------------
    # ---------------------删除制定---------------------
    def Deletes_the_designation_threading(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = result.split("\n")  # 遇见回车就

        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        try:
            self.Process_Get.edit_undo()  # 清空内容
        except:
            pass

        self.Process_Get.insert(tk.END, "正在提取！\n")

        for i in result:
            if self.Backupfilescan_url.get() in i:
                self.Process_Get.insert(tk.END, "已经删除" + i.strip()+"\n")
                self.Process_Get.see(tk.END)  # 始终处于最底端
            else:
                self.Output_the_result.insert(tk.END, i + "\n")  # 叫编码结果输出出来
                self.Output_the_result.see(tk.END)  # 始终处于最底端

        self.Process_Get.insert(tk.END, "完成！\n")  # 叫编码结果输出出来

    def Deletes_the_designation(self):


        def start():
            # 定义线程对象a函数
            t = threading.Thread(target=self.Deletes_the_designation_threading)
            # 启动线程
            t.start()

        self.Input_box()
        self.Output_box()
        self.Process_box()
        # 生成动态字符串
        self.Backupfilescan_url = tk.StringVar()

        ttk.Label(self.Input_right,
                  text="说明：指定要删除的会删除一行",
                  bootstyle="success").grid(row=0,
                                            column=1,
                                            sticky=tk.W)
        ttk.Entry(self.Input_right,
                  textvariable=self.Backupfilescan_url,
                  bootstyle="success",
                  width=30).grid(row=0,
                                 column=2,
                                 sticky=tk.W)
        label_1 = ttk.Button(self.Input_right,
                             text="开始",
                             command=start,
                             bootstyle="success")
        label_1.grid(row=0,
                    column=3,
                    sticky=tk.W)


    # ---------------------删除制定---------------------
    # ---------------------输出---------------------
    def Output_box(self):
        Output_Text = ttk.LabelFrame(self.top,
                                      text="输出",
                                      bootstyle="success")
        Output_Text.place(relx=0.603,# 左边
                        rely=0.1,# 上边
                          relwidth=0.393, # 右边
                          relheight=0.9) # 下边
       # --------------------------输出和滚动条----------------------------
        # 创建一个滚动条控件，默认为垂直方向
        go_out = ttk.Scrollbar(Output_Text, bootstyle="success")

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        go_out.pack(side=RIGHT,fill=Y)

        # 设置文本框控件
        self.Output_the_result = ttk.Text(Output_Text,
                                   #yscrollcommand=go_out.set,  # 调用滚动条
                                   undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.Output_the_result.place(relwidth=0.98,
                              relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.Output_the_result.config(font=font1, foreground='#008B00')  # 颜色




        # self.Output_the_result.insert(tk.END,
        #                        f"""{'*' * 80}\n\n\n作者：w啥都学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        #
        # 使用 command 关联控件的 yview、xview方法
        go_out.config(command=self.Output_the_result.yview)
        self.Output_the_result.config(yscrollcommand=go_out.set)  # 将滚动条关联到文本框
    # ---------------------输出---------------------

    # ---------------------输入---------------------
    def Input_box(self):

        self.Input_right = ttk.LabelFrame(self.top,
                                      text="选择要删除的",
                                      bootstyle="success")
        self.Input_right.place(relx=0.205,# 左边
                        rely=0.1,# 上边
                          relwidth=0.393, # 右边
                          relheight=0.66) # 下边

        Input_Text = ttk.LabelFrame(self.Input_right,
                                      text="输入",
                                      bootstyle="success")
        Input_Text.place(relx=0,# 左边
                            rely=0.08,# 上边
                              relwidth=1, # 右边
                              relheight=0.92) # 下边
        # --------------------------输出和滚动条----------------------------
        # 创建一个滚动条控件，默认为垂直方向
        Read = ttk.Scrollbar(Input_Text,
                             bootstyle="success")

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        Read.pack(side=RIGHT,
                  fill=Y)

        # 设置文本框控件
        self.Enter_Get = ttk.Text(Input_Text,
                                   #yscrollcommand=Read.set,  # 调用滚动条
                                   undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.Enter_Get.place(relwidth=0.98,
                              relheight=1)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.Enter_Get.config(font=font1, foreground='#008B00')  # 颜色


        # self.Enter_Get.insert(tk.END,
        #                        f"""{'*' * 80}\n\n\n作者：w啥都\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\nn\n\n\n\学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        #

        # 使用 command 关联控件的 yview、xview方法
        Read.config(command=self.Enter_Get.yview)
        self.Enter_Get.config(yscrollcommand=Read.set)  # 将滚动条关联到文本框
    # ---------------------输入---------------------

    def Process_box(self):
        Process_Text = ttk.LabelFrame(self.top,
                                      text="输出过程",
                                      bootstyle="success")
        Process_Text.place(relx=0.205,# 左边
                        rely=0.76,# 上边
                          relwidth=0.393, # 右边
                          relheight=0.24) # 下边
        # --------------------------输出和滚动条----------------------------
        # 创建一个滚动条控件，默认为垂直方向
        Read = ttk.Scrollbar(Process_Text, bootstyle="success")

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        Read.pack(side=RIGHT,fill=Y)

        # 设置文本框控件
        self.Process_Get = ttk.Text(Process_Text,
                                   #yscrollcommand=Read.set,  # 调用滚动条
                                   undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.Process_Get.place(relwidth=0.98,
                              relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.Process_Get.config(font=font1, foreground='#008B00')  # 颜色


        # self.Enter_Get.insert(tk.END,
        #                        f"""{'*' * 80}\n\n\n作者：w啥都\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\\n\nn\n\n\n\学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        #

        # 使用 command 关联控件的 yview、xview方法
        Read.config(command=self.Process_Get.yview)
        self.Process_Get.config(yscrollcommand=Read.set)  # 将滚动条关联到文本框

    def main(self,top):
        self.top=top
        # 显示线
        fofa_right = ttk.LabelFrame(top, text="实用工具", bootstyle="secondary")
        fofa_right.place(rely=0.1,# 上边
                         relwidth=1, # 右边
                         relheight=1) # 下边


        Utilities_right = ttk.LabelFrame(top, text="实用工具", bootstyle="success")
        Utilities_right.place(rely=0.1,# 上边
                              relwidth=0.2, # 右边
                              relheight=1.0) # 下边




        label_1 = ttk.Button(Utilities_right,
                             text="过滤删除重复的",
                             bootstyle="success-outline",
                             command=self.Remove_duplicates,
                             width=28,)
        label_1.grid(row=1,
                     column=1,
                     pady=9, )  # 位置

        label_1 = ttk.Button(Utilities_right,
                             text="过滤删除文件里面空白",
                             bootstyle="success-outline",
                             command=self.Delete_the_blank,
                             width=28,)
        label_1.grid(row=2,
                     column=1,
                     pady=9, )  # 位置


        label_1 = ttk.Button(Utilities_right,
                             text="过滤URL分割域名/IP(不带http://)",
                             bootstyle="success-outline",
                             command=self.Interface_dns,
                             width=28,)

        label_1.grid(row=3,
                     column=1,
                     pady=9, )  # 位置

        label_1 = ttk.Button(Utilities_right,
                             text="过滤URL分割域名/IP(带http://)",
                             bootstyle="success-outline",
                             command=self.Interface_http,
                             width=28,)
        label_1.grid(row=4,
                     column=1,
                     pady=9, )  # 位置

        label_1 = ttk.Button(Utilities_right,
                             text="删除自己指定过滤",
                             bootstyle="success-outline",
                             command=self.Deletes_the_designation,
                             width=28,)
        label_1.grid(row=5,
                     column=1,
                     pady=9, )  # 位置

if __name__ == '__main__':
    # 调用Tk()创建主窗口
    top = ttk.Window(themename="darkly")
    import os
    # top = ttk.Tk()··
    top.geometry('1250x680')
    # icon = PhotoImage(file="lib/avatar.ico")
    # top.tk.call('wm', 'iconphoto', top._w, icon)
    # 给主窗口起一个名字，也就是窗口的名字
    top.title('码小工具')
    tool = tool()
    tool.main(top)
    top.mainloop()