import requests
from lxml import etree
import base64
import time
from conf import config  # 配置文件
import ttkbootstrap as ttk

# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import choose_color_2, UseStyle


GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI

def current_time():
    return UseStyle(time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime()), fore='blue')


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['fofa'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP + '\n'))  # 写入
    Searchresults_document.close()  # 关闭文件


# 如果搜索结果多执行
def Multiple(Judge_page, coding, headers, speed):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI



    if GUT_Sure == 1:
        GUT_output.insert(ttk.END, "\n搜索结果有" + Judge_page + "页\n")
    else:
        print(current_time() + "搜索结果有" + Judge_page + "页")
    time.sleep(speed)  # 停顿一下
    recording = 0
    for all in range(1, int(Judge_page)):
        # 速度
        time.sleep(speed)
        if GUT_Sure == 1:
            GUT_output.insert(ttk.END, "[*]现在提取是第" + str(all) + "页\n")
        else:
            print(choose_color_2(current_time() + "[*]现在提取是第" + str(all) + "页"))
        # 逐个的页面提取
        html = requests.get(F'https://fofa.info/result?qbase64={str(coding)}&page={str(all)}&page_size=10', headers=headers)
        html = etree.HTML(html.text)
        divs = html.xpath(r'//span/a/@href')  # 语法
        for results_IP in divs:

            if GUT_Sure == 0:
                print(current_time() + choose_color_2("[*]第" + str(all) + "页----" + "IP地址是" + str(results_IP)))
            elif GUT_Sure == 1:
                GUT_output.insert(ttk.END, f"[*]第{str(all)} 页--IP地址是{str(results_IP)}\n" )

            Searchresults(results_IP)
            recording += 1

        # 循环50次就停止
        if recording >= 50:
            GUT_output.insert(ttk.END, f"\n普通用户只能放我50条信息")
            print(current_time() + choose_color_2("普通用户只能放我50条信息"))
            break


# 分析查询到结果判断是否是一页
def Determine(html, headers, coding, speed):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI

    try:
        html = etree.HTML(html.text)
        Judge_page  = html.xpath(r'//ul[@class="el-pager"]/li[last()]/text()')  # 查看是否有页数
        if Judge_page:  # 如果搜索结果多进行循环一个一个页面的读取
            Multiple(Judge_page[0], coding, headers, speed)
        else:
            if GUT_Sure == 1:  # 是GUI输出
                GUT_output.insert(ttk.END,"搜索结果就一页！\n")
            else:
                print(current_time() + choose_color_2("搜索结果就一页！"))
            divs = html.xpath(r'//span/a/@href')  # 探测IP
            for results_IP in divs:
                if GUT_Sure == 1:  # 是GUI输出
                    GUT_output.insert(ttk.END, f"[*]页IP地址是{str(results_IP)}\n")
                else:
                    print(current_time() + choose_color_2("[*]页----IP地址是" + str(results_IP)))
                Searchresults(results_IP)
    except Exception as bc:
        print(current_time() + "出差了：" + str(bc))


# 第一次请求
def cfq_insert_request(Cookie, coding, speed):
    url="https://fofa.info/result?qbase64=" + str(coding)
    headers = {  # 定义User-Agent请求头，用键值对的方式
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        'Cookie':Cookie
    }
    # 请求
    html = requests.get(url,headers=headers)
    # 分析查询到结果判断是否是一页
    Determine(html, headers, coding, speed)


# 保存我的输入的fofa_token值
def fofa_token():
    i = str(input(choose_color_2("输入'1'用上一次的Fofa的Cookie值:")))
    Cookie_fofa_token = 0
    if i == '1':
        fofa_token_document = open("fofa_token.txt", 'r')  # 读文件
        Cookie_fofa_token = fofa_token_document.readline()  # 读取文件的API
        fofa_token_document.close()  # 关闭文件
    else:
        Cookie_fofa_token = input(choose_color_2("Fofa请输入Cookie值："))  # 输入
        fofa_token_document = open("fofa_token.txt", 'w')  # 打开文件写的方式
        fofa_token_document.write(Cookie_fofa_token)  # 写入
        fofa_token_document.close()  # 关闭文件
    print("""
      __        __            _       _     _                   
     / _| ___  / _| __ _     / \   __| | __| |_ __ ___  ___ ___ 
    | |_ / _ \| |_ / _` |   / _ \ / _` |/ _` | '__/ _ \/ __/ __|
    |  _| (_) |  _| (_| |  / ___ \ (_| | (_| | | |  __/\__ \__ \.
    |_|  \___/|_|  \__,_| /_/   \_\__,_|\__,_|_|  \___||___/___/

                                    *fofa提取IP脚本
                                    *作者：赵赛赛
                                    *扫描速度快对方可能会屏蔽IP的
        """)
    return Cookie_fofa_token


def Interface(z, Cookie):
    if Cookie == None or Cookie == '':  # 使用默认Cookie
        print(current_time() + "当前你使用的是config.py里面的默认Cookie")
        Cookie = config.SeriousConfig['fofa']
    print(current_time() + "Cookie值是：" + Cookie)
    speed = 1
    print(current_time() + choose_color_2("你输入的是：" + z))
    print(current_time() + choose_color_2("[*]扫描结果会保存到result/fofa/fofa.txt文件"))
    # base64编码
    coding = base64.b64encode(z.encode('utf-8')).decode("utf-8")
    # 请求
    cfq_insert_request(Cookie, coding, speed)


def GUI(url, Cookie,speed, result):
    global GUT_output
    global GUT_Sure
    GUT_output=result # 输出到GUI
    GUT_Sure=1  # 判断是否用到GUI


    if Cookie == None or Cookie == '':  # 使用默认Cookie
        result.insert(ttk.END, "\n当前你使用的是config.py里面的默认Cookie\n")
        Cookie = config.SeriousConfig['fofa']
    result.insert(ttk.END, f"你输入的是：{url}\n扫描纯URL结果会保存到result/fofa/fofa.txt文件 \nCookie值是：{Cookie} \n{'*'*60}\n" )
    coding = base64.b64encode(url.encode('utf-8')).decode("utf-8")

    cfq_insert_request(Cookie, coding, speed)
    GUT_output.insert(ttk.END, f'\n完毕！')
    # for i in range(30):
    #     result.insert(ttk.END, '第' + str(i + 1) + '次\n')

# import  requests
# from lxml import etree
# import base64
# import time
#
#
#
# # 如果搜索结果多执行
# def Multiple(Judge_page,coding,headers,Cookie,speed):
#     print("[*]搜索结果有" + Judge_page + "页")
#     for all in range(1,int(Judge_page)):
#         time.sleep(speed)
#         print("[*]现在提取是第"+str(all)+"页")
#         html = requests.get('https://fofa.info/result?qbase64=' + coding+"&page="+str(all), headers=headers,cookies=Cookie)
#         html = etree.HTML(html.text)
#         divs = html.xpath(r'//span/a/@href')  # 语法
#         for i in divs:
#             print(i)
#
#
# def main():##界面
#     print("---------------------------------------------------")
#     print("\t _________ ____     __        __        \t\t")
#     print("\t|__  / ___/ ___|   / _| ___  / _| __ _  \t\t")
#     print("\t  / /\___ \___ \  | |_ / _ \| |_ / _` | \t\t")
#     print("\t / /_ ___) |__) | |  _| (_) |  _| (_| | \t\t")
#     print("\t/____|____/____/  |_|  \___/|_|  \__,_| \t\t\n\n")
#     print("*fofa信息收集探测工具")
#     print("*扫描速度快对方可能会屏蔽IP的")
#     print("---------------------------------------------------")
#     Cookie=input("Fofa登录后的值Cookie的fofa_token值：")
#     speed=int(input("请输入扫描速度："))
#     #base64编码
#     z=input("请输入要搜索的关键字：")
#     coding=base64.b64encode(z.encode('utf-8')).decode("utf-8")
# def Interface(z,Cookie):
#     speed = 1
#     coding = base64.b64encode(z.encode('utf-8')).decode("utf-8")
#     Cookie= {'Cookie': Cookie}
#     headers = {
#                 "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
#     }
#
#     print("[*]你输入的是"+z)
#     html=requests.get("https://fofa.info/result?qbase64="+str(coding),headers,cookies=Cookie)
#     html=etree.HTML(html.text)
#     try:
#
#         Judge_page=divs=html.xpath(r'//ul[@class="el-pager"]/li[last()]/text()')  # 查看是否有页数
#
#
#         if Judge_page: # 如果搜索结果多进行循环一个一个页面的读取
#             Multiple(Judge_page[0],coding,headers,Cookie,speed)
#         else:
#             print("[*]搜索结果就一页！")
#             divs = html.xpath(r'//span[@class="aSpan"]//@href')  # 探测IP
#             service = html.xpath(r'//p[@class="listSpanCont"]/a/text()')  # 用的服务器软件
#
#
#             order=0
#             for i in divs:
#                 print("[*]服务器IP地址是" + str(i)+"服务器软件"+service[order])
#                 order += 1
#
#     except Exception as bc:
#
#         print("出差了："+str(bc))
