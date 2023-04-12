# -*- coding:utf-8 -*-
import tkinter as tk
from PIL.ImageTk import PhotoImage
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import RIGHT
import base64
from urllib import parse
import re
import binascii
import hashlib



class tool:
    # Base64编码
    def Base64_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        encodestr = base64.b64encode(result.encode('utf-8'))
        outcome = str(encodestr, 'utf-8')
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # Base64解码
    def Base64_Decode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=base64.b64decode(result).decode("utf-8") # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # URL编码
    def Url_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=parse.quote(result, 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # URL解码
    def Url_Decode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=parse.unquote(result, 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # Unicode转中文
    def Unicode_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=result.encode('utf-8').decode("unicode_escape") # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # 中文转Unicode
    def Unicode_Decode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=result.encode("unicode_escape").decode() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来


    # 字符串转16进制
    def b16_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        result = bytes(result, "utf8")
        outcome=str(base64.b16encode(result), 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # 16进制转字符串
    def b16_Decode_class(self):

        result=str(self.Enter_Get.get("1.0","end")) # 获取输入的内容
        result = re.sub('\n', '', result) # 过滤\n
        outcome=str(base64.b16decode(result.upper()), 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # HEX转字符串
    def HEX_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        result = bytes(result, "utf8")
        outcome=str(binascii.hexlify(result), 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # 字符串转HEX
    def HEX_Decode_class(self):

        result=str(self.Enter_Get.get("1.0","end")) # 获取输入的内容
        result = re.sub('\n', '', result) # 过滤\n
        outcome=str(binascii.unhexlify(result.upper()), 'utf-8') # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # MD5加密小写32位
    def MD5small32_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        input_name = hashlib.md5()
        input_name.update(result.encode("utf-8"))
        outcome=(input_name.hexdigest()).lower() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # MD5加密大写32位
    def MD5big32_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        input_name = hashlib.md5()
        input_name.update(result.encode("utf-8"))
        outcome=(input_name.hexdigest()).upper() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # MD5加密小写16位
    def MD5small16_Encode_class(self):
        result = self.Enter_Get.get("1.0", "end")  # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        input_name = hashlib.md5()
        input_name.update(result.encode("utf-8"))
        outcome = (input_name.hexdigest())[8:-8].lower()  # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END, outcome)  # 叫编码结果输出出来

    # MD5加密大写16位
    def MD5big16_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        input_name = hashlib.md5()
        input_name.update(result.encode("utf-8"))
        outcome=(input_name.hexdigest())[8:-8].upper() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来
    # sha256加密
    def sha256_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=hashlib.sha256(result.encode('utf-8')).hexdigest() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来

    # SHA512加密
    def sha512_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=hashlib.sha512(result.encode('utf-8')).hexdigest() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来
    # SHA384加密
    def sha384_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=hashlib.sha384(result.encode('utf-8')).hexdigest() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来
    # SHA224加密
    def sha224_Encode_class(self):
        result=self.Enter_Get.get("1.0","end") # 获取输入的内容
        result = re.sub('\n', '', result)  # 过滤\n
        outcome=hashlib.sha224(result.encode('utf-8')).hexdigest() # 用这个自己写的函数进行编码
        try:
            self.Output_the_result.edit_undo()  # 清空内容
        except:
            pass
        self.Output_the_result.insert(tk.END,outcome) # 叫编码结果输出出来



    def Output_box(self,Coding_top):
        Output_Text = ttk.LabelFrame(Coding_top,
                                      text="结果",
                                      bootstyle="success")

        Output_Text.place(y=420,# 上下
                          relwidth=1,
                          relheight=0.38)
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
        self.Output_the_result.place(relwidth=0.99,
                              relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.Output_the_result.config(font=font1, foreground='#008B00')  # 颜色




        # self.Output_the_result.insert(tk.END,
        #                        f"""{'*' * 80}\n\n\n作者：w啥都学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        #

        # 使用 command 关联控件的 yview、xview方法
        go_out.config(command=self.Output_the_result.yview)


    def Input_box(self,Coding_top):
        Input_Text = ttk.LabelFrame(Coding_top,
                                      text="输入",
                                      bootstyle="success")

        Input_Text.place(y=190,# 上下
                          relwidth=1,# 右边
                          relheight=0.34) # 下边

        # --------------------------输出和滚动条----------------------------
        # 创建一个滚动条控件，默认为垂直方向
        Read = ttk.Scrollbar(Input_Text, bootstyle="success")

        # 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
        Read.pack(side=RIGHT,fill=Y)

        # 设置文本框控件
        self.Enter_Get = ttk.Text(Input_Text,
                                   #yscrollcommand=Read.set,  # 调用滚动条
                                   undo=True)  # 开启删除内容
        # 在主窗口内显示
        self.Enter_Get.place(relwidth=0.99,
                              relheight=1.0)

        # font1 = tk.font.Font(family='微软雅黑',size=24) # 设置字体
        font1 = tk.font.Font()
        self.Enter_Get.config(font=font1, foreground='#008B00')  # 颜色


        # self.Enter_Get.insert(tk.END,
        #                        f"""{'*' * 80}\n\n\n作者：w啥都学\nBlog地址：www.zssnp.top\ngitee项目地址：https://gitee.com/wZass/Full-Scanner\ngithub项目地址：https://github.com/Zhao-sai-sai/Full-Scanner\n\n\n{'*' * 80}""")
        #

        # 使用 command 关联控件的 yview、xview方法
        Read.config(command=self.Enter_Get.yview)

    def main(self,Coding_top):
        self.Input_box(Coding_top)
        self.Output_box(Coding_top)

        classification = ttk.LabelFrame(Coding_top,
                                      text="编码",
                                      bootstyle="success")

        classification.place(y=72,  # 上下
                             relwidth=1,
                             relheight=0.176)

        b1 = ttk.Button(classification,
                        text='Base64编码',
                        command=self.Base64_Encode_class,
                        bootstyle=SUCCESS) # 样式

        b1.grid(row=1,
                column=1,
                padx=1,
                pady=1) # 用于控制外边距


        b2 = ttk.Button(classification,
                        text='Base64解码',
                        command=self.Base64_Decode_class,
                        bootstyle=SUCCESS) # 样式
        b2.grid(row=2,
                column=1,
                padx=1,
                pady=1) # 用于控制外边距


        b3 = ttk.Button(classification,
                        text='URL编码',
                        command=self.Url_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b3.grid(row=1,
                column=2,
                padx=1,
                pady=1) # 用于控制外边距

        b3 = ttk.Button(classification,
                        text='URL解码',
                        command=self.Url_Decode_class,
                        bootstyle=SUCCESS) # 样式
        b3.grid(row=2,
                column=2,
                padx=1,
                pady=1) # 用于控制外边距


        b4 = ttk.Button(classification,
                        text='中文转Unicode',
                        command=self.Unicode_Decode_class,
                        bootstyle=SUCCESS) # 样式
        b4.grid(row=1,
                column=3,
                padx=1,
                pady=1) # 用于控制外边距

        b4 = ttk.Button(classification,
                        text='Unicode转中文',
                        command=self.Unicode_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b4.grid(row=2,
                column=3,
                padx=1,
                pady=1) # 用于控制外边距



        b5 = ttk.Button(classification,
                        text='ASCII字符串转16进制',
                        command=self.b16_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b5.grid(row=1,
                column=4,
                padx=1,
                pady=1) # 用于控制外边距

        b5 = ttk.Button(classification,
                        text='ASCII16进制转字符串',
                        command=self.b16_Decode_class,
                        bootstyle=SUCCESS) # 样式
        b5.grid(row=2,
                column=4,
                padx=1,
                pady=1) # 用于控制外边距

        b6 = ttk.Button(classification,
                        text='HEX转字符串',
                        command=self.HEX_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b6.grid(row=1,
                column=5,
                padx=1,
                pady=1) # 用于控制外边距

        b6 = ttk.Button(classification,
                        text='字符串转HEX',
                        command=self.HEX_Decode_class,
                        bootstyle=SUCCESS) # 样式
        b6.grid(row=2,
                column=5,
                padx=1,
                pady=1) # 用于控制外边距


        b7 = ttk.Button(classification,
                        text='MD5加密小写32位',
                        command=self.MD5small32_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b7.grid(row=1,
                column=6,
                padx=1,
                pady=1) # 用于控制外边距

        b7 = ttk.Button(classification,
                        text='MD5加密大写32位',
                        command=self.MD5big32_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b7.grid(row=2,
                column=6,
                padx=1,
                pady=1) # 用于控制外边距

        b7 = ttk.Button(classification,
                        text='MD5加密小写16位',
                        command=self.MD5small16_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b7.grid(row=1,
                column=7,
                padx=1,
                pady=1) # 用于控制外边距

        b7 = ttk.Button(classification,
                        text='MD5加密大写16位',
                        command=self.MD5big16_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b7.grid(row=2,
                column=7,
                padx=1,
                pady=1) # 用于控制外边距

        b8 = ttk.Button(classification,
                        text='SHA256加密',
                        command=self.sha256_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b8.grid(row=1,
                column=8,
                padx=1,
                pady=1) # 用于控制外边距
        b8 = ttk.Button(classification,
                        text='SHA512加密',
                        command=self.sha512_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b8.grid(row=2,
                column=8,
                padx=1,
                pady=1) # 用于控制外边距


        b8 = ttk.Button(classification,
                        text='SHA384加密',
                        command=self.sha384_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b8.grid(row=1,
                column=9,
                padx=1,
                pady=1) # 用于控制外边距

        b8 = ttk.Button(classification,
                        text='SHA224加密',
                        command=self.sha224_Encode_class,
                        bootstyle=SUCCESS) # 样式
        b8.grid(row=2,
                column=9,
                padx=1,
                pady=1) # 用于控制外边距
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
    tool=tool()
    tool.main()
    top.mainloop()