import os
import time
from flask import Flask, request
import requests
import datetime
import logging
import json
import threading  # 预防卡住
import ttkbootstrap as ttk
from conf import config  # 配置文件

token = 1 # 记录请求多少次


app = Flask(__name__)

@app.route('/webhook', methods=['POST'])

def xray_webhook():
    vuln = request.json
    #print(vuln)
    content = f"""
    xray 发现了新漏洞
    ---------------
    插件: {vuln['data']["plugin"]}
    漏洞类型: {vuln["type"]}
    漏洞地址: {vuln['data']["target"]["url"]}
    发现时间: {str(datetime.datetime.fromtimestamp(vuln["data"]["create_time"] / 1000))}
    ---------------
    请及时查看和处理
    """

    try:
        push_dingding_group(content)
    except Exception as e:
        logging.exception(e)
    print(content)
    return 'ok'


def push_dingding_group(content):
    global token
    headers = {"Content-Type": "application/json"}
    # 消息类型和数据格式参照钉钉开发文档
    data = {"msgtype": "markdown", "markdown": {"title": "xray 发现了新漏洞"}}
    data['markdown']['text'] = content

    r = requests.post(f"https://oapi.dingtalk.com/robot/send?access_token={token}", data=json.dumps(data),
                      headers=headers)
    print(r.text)




def current_time():
    return time.strftime("%Y_%m_%d年%H_%M_%S时", time.localtime())
def Xray_Rad_and_Xray_invoke_dd():

    os.system(f"cd leakscan/xray && konsole  -e './xray webscan --listen 127.0.0.1:7777  --webhook-output http://127.0.0.1:5000/webhook  --html-output ../../result/xray/{current_time()}.html'")
def Xray_Rad_and_Xray_invoke():
    os.system(f"cd leakscan/xray && konsole  -e './xray webscan --listen 127.0.0.1:7777 --html-output ../../result/xray/{current_time()}.html'")

def rad_Rad_and_Xray_invoke(RXURL):
    time.sleep(7)
    os.system(f"cd leakscan/xray && konsole  -e './rad -t {str(RXURL)} -http-proxy 127.0.0.1:7777'")



def run():
    app.run()



def main(RXURL,MRX,RXDD):
    print("xray扫描结果会保存在：result/xray")
    if RXDD==None:
        if config.SeriousConfig['dingtalk'] !='':
            RXDD=config.SeriousConfig['dingtalk']
            print("使用config的配置文件的token")
    #print(RXURL,MRX,RXDD)
    if RXDD !=None : # 是否带钉钉推送
        global token
        token=RXDD # 钉钉的token

        # 启动POST请求接收
        # 定义线程 预防卡
        TRXDD = threading.Thread(target=run, args=())
        # 启动线程
        TRXDD.start()


        # 启动 xray
        t1 = threading.Thread(target=Xray_Rad_and_Xray_invoke_dd, args=())
        # 启动线程
        t1.start()
    else:
        # 启动 xray
        t1 = threading.Thread(target=Xray_Rad_and_Xray_invoke, args=())
        # 启动线程
        t1.start()

    if RXURL !=None:
        # 启动 rad
        rad_Rad_and_Xray_invoke(RXURL)


    if MRX != None:
        for i in open(MRX):
            rad_Rad_and_Xray_invoke(i.rstrip())



def main_dingtalk_gui(MRX,RXDD,result):

    result.insert(ttk.END,"xray扫描结果会保存在：result/xray\n")

    if RXDD !='' : # 是否带钉钉推送
        global token
        token=RXDD # 钉钉的token

        # 启动POST请求接收
        # 定义线程 预防卡
        TRXDD = threading.Thread(target=run, args=())
        # 启动线程
        TRXDD.start()


        # 启动 xray
        t1 = threading.Thread(target=Xray_Rad_and_Xray_invoke_dd, args=())
        # 启动线程
        t1.start()
    else:
        result.insert(ttk.END, f"请输入钉钉的token\n")
        return
    result.insert(ttk.END, f"正在加载Xray等待一会！\n")

    if MRX != '':
        for i in open(MRX):
            result.insert(ttk.END, f"正在扫描：{i.rstrip()}\n")
            rad_Rad_and_Xray_invoke(i.rstrip())
            result.insert(ttk.END, f"rad完成：{i.rstrip()}\n")


def main_gui(MRX,result):
    if MRX !='':
        # 启动 xray
        t1 = threading.Thread(target=Xray_Rad_and_Xray_invoke_dd, args=())
        # 启动线程
        t1.start()

        for i in open(MRX):
            result.insert(ttk.END, f"正在扫描：{i.rstrip()}\n")
            rad_Rad_and_Xray_invoke(i.rstrip())
            result.insert(ttk.END, f"rad完成：{i.rstrip()}\n")


def main_Single__gui(RXURL,result):
    if RXURL !='':
        # 启动 xray
        t1 = threading.Thread(target=Xray_Rad_and_Xray_invoke_dd, args=())
        # 启动线程
        t1.start()

        result.insert(ttk.END, f"正在扫描：{RXURL}\n")
        # 启动 rad
        rad_Rad_and_Xray_invoke(RXURL)
        result.insert(ttk.END, f"rad完成：{RXURL}\n")