#!/usr/bin/python
# -*- coding: UTF-8 -*-

from lib import Auxiliary
from lib.choose_model import Big_Category
from lib.choose import choose_color_2
from rich.console import Console
from rich.table import Table
from rich import box
from lib.cmdline import cmdline  # 图标



# 被动信息判断
def Passive_Options_Judge(Judge):
    Auxiliary.Sundries().total_tips() # 提示

    if Judge=='Q':
        Auxiliary.Terminal_clear()  # 终端清空
        print("退出了")
        return
    if Judge=='q': # 返回上一层
        Big_Category.Category()

    elif Judge=='1': # fofa查询
        from collect import  fofa
        url=input(choose_color_2('请输入目标地址：'))
        Cookie = input(choose_color_2('请输Cookie值回车用config.py的值：'))
        fofa.Interface(url,Cookie)

    elif Judge=='2': # shodan
        from collect import shodan
        host=input(choose_color_2('请输入目标地址：'))
        API = input(choose_color_2('请输API(如果不输入直接回车默认使用配置config文件的)：'))
        shodan.shod(host,API)

    elif Judge == '3':  # shodan
        args = cmdline.help_h()

        from collect import req_whois
        args.whois=input(choose_color_2('请输入查询的域名：'))
        req_whois.Interface(args)

# 被动信息收集选择
def Passive_Information_Gathering():

    Auxiliary.Sundries().total_tips() # 提示


    table = Table(title="被动信息收集", box=box.HORIZONTALS, style="yellow")

    table.add_column("序列", justify="right", style="green", min_width=3, no_wrap=True)
    table.add_column("名字", style="blue", min_width=51, justify="right")


    table.add_row("|1|", "fofa子域名探测")
    table.add_row("|2|", "shodan信息收集")
    table.add_row("|3|", "whois查询")
    table.add_row("|q|", "返回上一层")
    table.add_row("|Q|", "退出")

    console = Console()
    console.print(table)
    Passive_Options_Judge(input(" 选择 > "))