# -- coding:UTF-8 --
import requests
from lib.choose import UseStyle # 设置颜色
import argparse
from lxml import etree
import time
import urllib3
from urllib.parse import quote,urlparse # urlparse提取url的dns
from conf import config # 配置文件
import ttkbootstrap as ttk

urllib3.disable_warnings()  # 忽略https证书告警

GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI

# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['bing'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件


def Climb_bing(keywords,amount):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI

    keywords = keywords.replace(' ', '+') # 空格用+来代替
    keywords=quote(keywords, 'utf-8') # 进行url编码

    for i in range(0, int(amount)):
        if GUT_Sure==1:
            GUT_output.insert(ttk.END, f'{"*" * 60}\n正在爬取第：{i+1}页\n')
        else:
            print(f'\033[0;33m {"*" * 60}\033[0m\n正在爬取第：{i+1}页')
        url = f"https://cn.bing.com/search?q={keywords}&go=%E6%90%9C%E7%B4%A2&qs=ds&first={i}1&FORM=PERE1"
        try:
            html = requests.get(url=url, headers=config.HeadersConfig, verify=False, timeout=5)
            # //div[@id="search"]//div//div//div//div//div//div/a[@data-ved]/@href
            html = etree.HTML(html.text)

            divs1 = html.xpath(r'//div/h2/a/@href')  # 语法
            divs2 = html.xpath(r'//div/h2/a/text()')  # 语法


            for i in range(int(len(divs1))):
                if GUT_Sure == 1:
                    GUT_output.insert(ttk.END, f"标题：《{divs2[i]}》\n地址：{divs1[i]}\n")
                else:
                    print(UseStyle("标题：《"+divs2[i]+"》",fore='red')+"\n地址："+divs1[i]) # 输出爬的结果

                Searchresults(divs1[i])

        except Exception as bc:
            GUT_output.insert(ttk.END, "\n有错误！错误提示" + str(bc))
            print("有错误！错误提示" + str(bc))


def Interface(args):
    keywords=args.bing
    if args.bingm == None:
        amount=100000
    else:
        amount = args.bingm

    print(UseStyle(f"\n扫描结果保存在{config.Savelocation['bing']}文件夹下\n搜索的关键字是：{keywords}\n页数：{amount}",fore='red')+f'\n\033[0;33m {"*" * 60}')
    time.sleep(3)  # 暂停 3 秒
    Climb_bing(keywords, amount)

def GUI(keywords, amount, result):

    global GUT_output
    global GUT_Sure
    GUT_output=result # 输出到GUI

    GUT_Sure=1  # 判断是否用到GUI
    if amount == '':
        amount=100000


    GUT_output.insert(ttk.END,
                      f"扫描的纯URL保存在{config.Savelocation['bing']}文件夹下\n搜索的关键字是：{keywords}\n输入的页数：{amount}"+f'\n{"*" * 60}\n')
    GUT_output.insert(ttk.END, f'启动查询请稍候！\n')
    Climb_bing(keywords, amount)
    GUT_output.insert(ttk.END,f'完毕！')
if __name__ == '__main__':
    pass
    #combination("a",b"")