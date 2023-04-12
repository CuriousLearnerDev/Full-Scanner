import shodan
import time
from conf import config
# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import choose_color_2,UseStyle
from lib.Auxiliary import Sundries


import ttkbootstrap as ttk
GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI

def current_time():
    return UseStyle(time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime()),fore='blue')

# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['shodan'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# API
def shodan_API():
    i = str(input("请输入"))
    # 输入API
    Shodan_api = 0
    if i == '1':
        API_document = open("API.txt", 'r')  # 读文件
        Shodan_api = API_document.readline()  # 读取文件的API

        API_document.close()  # 关闭文件
    else:
        Shodan_api = input("请输入自己的shodan的API：")
        API_document = open("API.txt", 'w')
        API_document.write(Shodan_api)
        API_document.close()
        api = shodan.Shodan(Shodan_api)

    print('''
             _               _
         ___| |__   ___   __| | __ _ _ __
        / __| '_ \ / _ \ / _` |/ _` | '_ \
        \__ \ | | | (_) | (_| | (_| | | | |
        |___/_| |_|\___/ \__,_|\__,_|_| |_|

        * 信息收集
        * 1. 输入用第一次的API
         ''')

    # api = shodan_API()
    host = str(input("请输入目标地址："))
    return api


def shod(host,Shodan_api):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI

    try:
        if Shodan_api==None or Shodan_api=='': # 查看你的PCT是否输入参数,没有输入执行
            Shodan_api=config.SeriousConfig['shodan']



        if GUT_Sure == 1:  # 输出到GUI
            GUT_output.insert(ttk.END, f"IP地址是：{host}\n指定的API内容：{str(Shodan_api)}\n扫描结果会保存到result/shodan/shodan.txt文件\n{'*'*60}\n")
        else:
            print(choose_color_2(f"IP地址是：{host}\n指定的API内容：{str(Shodan_api)}\n扫描结果会保存到result/shodan/shodan.txt文件\n{'*'*60}\n"))

        api = shodan.Shodan(Shodan_api)

        resultip = api.host(host)

        for result in resultip['data']:

            # 预防报错
            try:
                domains=result['domains']
            except:
                result['domains']=' '
                domains=result['domains']
            try:
                org=result['org']
            except:
                result['org'] = ' '
                org = result['org']


            try:
                os=result['os']
            except:
                result['os'] = ' '
                os = result['os']


            try:
                port=result['port']
            except:
                result['port']=' '
                port = result['port']


            try:
                product=result['product']
            except:
                result['product']=' '
                product = result['product']


            try:
                data=result['data']
            except:
                result['data']=' '
                data = result['data']


            try:
                timestamp=result['timestamp']
            except:
                result['timestamp']=' '
                timestamp = result['timestamp']


            try:
                country_name=result["location"]['country_name']
            except:
                result["location"]['country_name']=' '
                country_name = result["location"]['country_name']

            Sure =f'\n域名: {domains}\n云提供商: {org}\n操作系统: {os}\n放的端口: {str(port)}\n使用的服务器软件: {product}\n响应信息: {data}\n爬曲时间: {timestamp}\n国家是: {country_name}'
            if GUT_Sure == 1:  # 输出到GUI
                GUT_output.insert(ttk.END, Sure)
            else:
                searchresults=current_time()+choose_color_2(f'\n域名: {domains}\n云提供商: {org}\n操作系统: {os}\n放的端口: {str(port)}\n使用的服务器软件: {product}\n响应信息: {data}\n爬曲时间: {timestamp}\n国家是: {country_name}')
                print(searchresults)
            Searchresults(Sure)
            print()
    except Exception as bc:
        print(current_time()+"有错误！\n错误提示"+str(bc))
def GUI(host,Shodan_api,result):
    global GUT_output
    global GUT_Sure
    GUT_output=result # 输出到GUI
    GUT_Sure=1  # 判断是否用到GUI
    GUT_output.insert(ttk.END, f'启动查询请稍候！\n')
    shod(host, Shodan_api)
    GUT_output.insert(ttk.END, f'\n完毕！')
