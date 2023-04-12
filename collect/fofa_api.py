import requests
import base64
import urllib3
import time
from conf import config  # 配置文件
# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import choose_color_2, UseStyle
import ttkbootstrap as ttk


urllib3.disable_warnings()  # 忽略https证书告警




# 提取出来的结果保存起来
# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['fofa'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件


def current_time():
    return UseStyle(time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime()), fore='blue')


def Multiple(target,email,api_key,size):

    api = f'https://fofa.info/api/v1/search/all?email={email}&key={api_key}&qbase64={target}&size={size}'
    response = requests.get(api)

    try:
        results = response.json()["results"]
        print(UseStyle(f"{'*'*60}\n\n\n共搜索出来{len(results)}条记录",fore='red'))
        print("*" * 30)
        for addr in results:
            print("\t"+addr[0])
            Searchresults(addr[0])
    except:
       print(f"\n*********\nkey或者邮箱错误！\n*********")


def Interface(target,api_key,email,size):
    print(current_time() + UseStyle("[*]扫描结果会保存到result/fofa/",fore='green'))
    print(current_time() + UseStyle("你输入的是：" + target,fore='green'))

    # base64编码
    target = base64.b64encode(target.encode('utf-8')).decode("utf-8")

    if size==None: # 默认搜索多少条
        size=100

    if email == None and  api_key == None : # 判断有没有输入

        # 没有输入读取文件内容
        if config.SeriousConfig['fofa_api']['key'] == '' and config.SeriousConfig['fofa_api']['email']== '':
            print('请输入key或者email、如果不想每次都指定可以去config.py文件里面添加')
            return
        else:
            api_key=config.SeriousConfig['fofa_api']['key']
            email=config.SeriousConfig['fofa_api']['email']
            print(current_time() + UseStyle("当前你使用的是config.py里面的默认key、email",fore='green'))
            print(current_time() + UseStyle(f"key值是：{api_key}",fore='green'))
            print(current_time() + UseStyle(f"email值是：{email}",fore='green'))

            Multiple(target, email, api_key, size)
    else:
        if email != None and api_key != None:  # 判断有没有输入
            print(current_time() + UseStyle(f"key值是：{api_key}",fore='green'))
            print(current_time() + UseStyle(f"email值是：{email}",fore='green'))
            Multiple(target, email, api_key, size)
        else:
            print("你少输入一个重要的参数")




def Multiple_GUI(target,email,api_key,size,result):

    api = f'https://fofa.info/api/v1/search/all?email={email}&key={api_key}&qbase64={target}&size={size}'
    response = requests.get(api)
    try:
        results = response.json()["results"]
        result.insert(ttk.END, f"{'*'*60}\n\n\n共搜索出来{len(results)}条记录\n")
        result.insert(ttk.END,f'{"*" * 30}\n')
        for addr in results:
            result.insert(ttk.END, f"{addr[0]}\n")
            Searchresults(addr[0])
    except:
        result.insert(ttk.END, f"\n*********\nkey或者邮箱错误！\n*********")


def GUI(target,api_key,email,size,result):

    result.insert(ttk.END, "[*]扫描结果会保存到result/fofa/\n")
    result.insert(ttk.END, f"你输入的是：{target}\n")

    # base64编码
    target = base64.b64encode(target.encode('utf-8')).decode("utf-8")



    if email == '' and  api_key == '' : # 判断有没有输入

        # 没有输入读取文件内容
        if config.SeriousConfig['fofa_api']['key'] == '' and config.SeriousConfig['fofa_api']['email']== '':
            result.insert(ttk.END, '请输入key或者email、如果不想每次都指定可以去config.py文件里面添加\n')
            return
        else:
            api_key=config.SeriousConfig['fofa_api']['key']
            email=config.SeriousConfig['fofa_api']['email']
            result.insert(ttk.END, "当前你使用的是config.py里面的默认key、email\n")
            result.insert(ttk.END,f"key值是：{api_key}\n")
            result.insert(ttk.END,f"email值是：{email}\n")

            Multiple_GUI(target, email, api_key, size,result)
    else:
        if email != None and api_key != None:  # 判断有没有输入
            result.insert(ttk.END,f"key值是：{api_key}\n")
            result.insert(ttk.END,f"email值是：{email}\n")
            Multiple_GUI(target, email, api_key, size,result)
        else:
            result.insert(ttk.END,"你少输入一个重要的参数\n")
