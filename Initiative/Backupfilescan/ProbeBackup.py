import requests
#from conf import config
import queue
import threading
from urllib import error
import urllib.request
from urllib.parse import quote # urllib请求url里面带中文就会报错用这个抱住就可以了
import sys
sys.path.append("../../") # 解决上级库文件

from lib.Auxiliary import current_time
from conf import config # 配置文件
import re
import time
# choose_color_2  随机颜色 UseStyle指定颜色
from lib.choose import UseStyle,choose_color_2
import ttkbootstrap as ttk


GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI


count = 1 # 记录请求多少次

schedule=0 # 数数
pl=0 # 记录批量扫描的数量

def current_time_GUI():
    return time.strftime("[%Y-%m-%d_%H:%M:%S]: [*]", time.localtime())

# 批量扫描
def Batch_scan(path):
    Batch=[]
    i = 1
    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(path, encoding="UTF-8")

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        i += buffer.count('\n')
    global GUT_Sure  # 判断是否用到GUI
    global GUT_output  # 输出到GUI
    if GUT_Sure == 1:
        GUT_output.insert(ttk.END,f"{'-'*5}文件一共有"+str(i)+f"条目标{'-'*5}\n")

    else:
        print(UseStyle(f"{'-'*20}文件一共有"+str(i)+f"条目标{'-'*20}",fore='yellow'))
    # 叫每一行内容都保存到search_url中
    for i in open(path, encoding="UTF-8"):
        Batch.append(i.rstrip())

    return Batch

# 读取字典文件内容
def Read_dictionary(path):
    global schedule

    # 叫文件内容变成
    search_url=queue.Queue()
    thefile=open(path, encoding="UTF-8")

    # 统计有多少行
    while True:
        buffer = thefile.read(1024 * 8192)
        if not buffer:
            break
        schedule += buffer.count('\n')
    global GUT_Sure  # 判断是否用到GUI
    global GUT_output  # 输出到GUI
    if GUT_Sure == 1:
        GUT_output.insert(ttk.END,"使用的字典是"+path+"\n")
        GUT_output.insert(ttk.END,f"文件一共有"+str(schedule)+"条\n\n\n")
    else:
        print(UseStyle("文件一共有"+str(schedule)+"条",fore='yellow'))
    # 叫每一行内容都保存到search_url中
    for i in open(path, encoding="UTF-8"):
        search_url.put(i.rstrip())

    return search_url


# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['ProbeBackup'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

# 单位换算
def covertFukeSize(size):

    size=int(size)

    kb = 1024
    mb = kb * 1024
    gb = mb * 1024
    tb = gb * 1024

    if size >= tb:
        return "文件小%.1f TB" % float(size / tb)
    if size >= gb:
        return "文件小%.1f GB" % float(size / gb)
    if size >= mb:
        return "文件小%.1f MB" % float(size / mb)
    if size >= kb:
        return "文件小%.1f KB" % float(size / kb)
    else:
        return '文件小于1kb'



def ask(url,url_exists,proxies):
    HeadersConfig = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    global count
    while not url_exists.empty():
        searchurl=url_exists.get()

        try:
            # 原位输出
            #print(f"\r{current_time()} 进度: {count}/{schedule}",  end="\r")

            print(f"{current_time()}{count}/{schedule} 进度： {url+quote(searchurl)}")
            back = urllib.request.Request(url=url+quote(searchurl), headers=config.HeadersConfig,method='GET')


            # 是否使用代理
            if proxies != None:

                # 使用选择的代理构建代理处理器对象
                httpproxy_handler = urllib.request.ProxyHandler(proxies)

                # 通过 urllib.request.build_opener(),创建自定义opener对象
                opener = urllib.request.build_opener(httpproxy_handler)

                #发送代理请求
                response = opener.open(back, timeout=7) # 代理请求
            else:
                response = urllib.request.urlopen(back, timeout=7)
            count += 1
            if response.status == 200:
                count += 1
                content = response.headers['content-length']
                content=covertFukeSize(content)
                print(UseStyle(f"{'*'*20}\n请求这个备份文件存在：" +url+ searchurl+f'文件大小：\t{content}\n{"*"*20}', fore='green'))
                Searchresults(url+searchurl+f'\t\t文件大小：{content}')

        except Exception as cw:
            if str(cw) in "HTTP Error 404: Not Found":  # 报错404的
                count += 1
            elif str(cw) in "<urlopen error [Errno 113] No route to host>":  # 报错超时的
                print('\n目标未7响应时间超时了！')
                break
            else:
                count += 1
                GUT_output.insert(ttk.END,f'\n未知错误：{cw}\n')


def ask_GUI(url,url_exists,proxies):
    global GUT_output  # 输出到GUI

    global count

    while not url_exists.empty():
        searchurl=url_exists.get()

        try:
            # 原位输出
            #print(f"\r{current_time()} 进度: {count}/{schedule}",  end="\r")

            GUT_output.insert(ttk.END,f"{count}/{schedule} 进度： {url+quote(searchurl)}\n")
            back = urllib.request.Request(url=url+quote(searchurl), headers=config.HeadersConfig,method='GET')


            # 是否使用代理
            if  ":" in  proxies:
                # 使用选择的代理构建代理处理器对象
                httpproxy_handler = urllib.request.ProxyHandler(proxies)

                # 通过 urllib.request.build_opener(),创建自定义opener对象
                opener = urllib.request.build_opener(httpproxy_handler)

                #发送代理请求
                response = opener.open(back, timeout=7) # 代理请求
            else:
                response = urllib.request.urlopen(back, timeout=7)
            count += 1
            if response.status == 200:
                count += 1
                content = response.headers['content-length']
                content=covertFukeSize(content)
                GUT_output.insert(ttk.END,f"{'*'*20}\n请求这个备份文件存在：" +url+ searchurl+f'文件大小：\t{content}\n{"*"*20}\n')
                Searchresults(url+searchurl+f'\t\t文件大小：{content}')

        except Exception as cw:
            if str(cw) in "HTTP Error 404: Not Found":  # 报错404的
                count += 1
            elif str(cw) in "<urlopen error [Errno 113] No route to host>":  # 报错超时的
                GUT_output.insert(ttk.END,'\n目标未7响应时间超时了！\n')
                break
            else:
                count += 1
                GUT_output.insert(ttk.END,f'\n未知错误：{cw}\n')
# 设置线程
def Thread(url,url_exists,T,proxies):
    global GUT_Sure  # 判断是否用到GUI

    if GUT_Sure == 1:
        threadpool = []
        for _ in range(int(T)):
            Threads = threading.Thread(target=ask_GUI, args=(url,url_exists,proxies, ))
            threadpool.append(Threads)
        for th in threadpool:
            th.start()
        for th in threadpool:
            threading.Thread.join(th)
    else:
        threadpool = []
        for _ in range(int(T)):
            Threads = threading.Thread(target=ask, args=(url,url_exists,proxies, ))
            threadpool.append(Threads)
        for th in threadpool:
            th.start()
        for th in threadpool:
            threading.Thread.join(th)


def splicing(url,url_s,segmentation,T,proxies):
    url_exists = queue.Queue()
    dictionary = ['index.php.txt',
                  'backup.zip',
                  'website.zip',
                  'web.zip',
                  'index.zip',
                  'wwwroot.zip',
                  'faisunzip.zip',
                  'wwwroot.rar',
                  'wwwroot.tar.gz',
                  'wwwroot.gz',
                  'wwwroot.sql.zip',
                  'back.zip',
                  'wwwroot.sql',
                  'www.zip',
                  'backup.zip',
                  'bbs.zip',
                  'www.tar.gz',
                  "我的.txt"]


    suffix = ['.zip',
              '.rar',
              '.tar.gz',
              '.sql.gz',
              '.7z',
              '.sql',
              '.tar.tgz',
              '.tar.bz2',
              '.gz',
              '.tar.xz',
              '.log.gz',
              '.log.bz2',
              '.log.xz',
              '.wim',
              '.lzh',
              '.bak',
              '.txt',
              '.old',
              '.jar',
              '.temp']

    # small = [chr(i) for i in range(97,123)] # a-z
    # calltaxi = [chr(i) for i in range(97, 123)]  # A-Z
    # number = [str(i) for i in range(0, 10)] # 0-9


    # for i in small:  # a-z
    #     for Extract_4 in suffix:
    #         url_exists.put(i+Extract_4)
    #
    # for i in calltaxi:  # A-Z
    #     for Extract_5 in suffix:
    #         url_exists.put(i + Extract_5)

    # for i in number:  # 0-9
    #     for Extract_6 in suffix:
    #         url_exists.put(i + Extract_6)

    for Extract_1 in suffix:# 域名拼接
        url_exists.put(url_s+Extract_1)

    for i in suffix: # 分割拼接
        for Extract_2 in segmentation:
            url_exists.put(Extract_2+i)

    for Extract_3 in dictionary:# 默认字典
        url_exists.put(Extract_3)

    global schedule
    schedule = str((len(url_exists.queue)))

    Thread(url,url_exists,T,proxies)


def fix(url,T,document,proxies):

    # # 判断是否有http头
    # if "http" in url:
    #     pass
    # else:
    # 自动添加协议头
    if url.startswith('http://') or url.startswith('https://'):
        if 'http://' in url:
            http = 'http://'
        elif 'https://' in url:
            http = 'https://'
    else:
        http = 'http://'
        judge_https = http + url.strip()


        # 判断是否是https
        response = urllib.request.urlopen(judge_https)
        if response.getcode() == 200:
            if response.url.startswith("https://"):
                url= "https://" + url.strip()
                http="https://"
            elif response.url.startswith("http://"):
                url = "http://" + url.strip()
                http = "http://"


    #return
    url_s = url.replace(http, '')
    if url[-1] != '/':
        url += '/' # 查看最后一个是否有/没有添加/

    url_s=re.sub('http://', '', url_s)
    url_s=re.sub('https://', '', url_s)

    if ':' in url_s:
        url_s=url_s.split(':')[0]
        segmentation=url_s.split('.')

    else:
        segmentation=url_s.split('.')
    if document==None or document=='':
        splicing(url,url_s,segmentation,T,proxies)
        return
    else:
        document_=Read_dictionary(document)
        print("使用的字典是"+document+"\n\n")
        Thread(url,document_,T,proxies)

def Interface(args):

    args.url=args.PB #URL
    args.many=args.PBm #  文件名  多个目标保存到一个文件里面进行批量扫描
    args.thread = args.PBt # 线程数
    args.document = args.PBd # 字典文件
    args.proxies = args.PBp #代理
    global pl
    global schedule
    global count

    if args.url !=None or args.many != None:
        if args.thread==None:
            args.thread=1

        # 设置代理
        if args.proxies != None:
             args.acting=args.proxies
             args.proxies= {
                "http": "http://" +args.acting ,
                "https": "http://" + args.acting
            }

        # 是否批量扫描
        if args.many == None: # 不批量扫描

            print(choose_color_2("扫描结果会保存到：result/ProbeBackup/文件夹里面\n你输入的目标地址是: " +
                                 args.url +
                                 '\n线程数是：' +
                                 str(args.thread) +
                                 "\n使用自动生成字典扫描！"+
                                 f'\n\033[0;33m {"—" * 60}\033[0m'))

            fix(args.url,args.thread,args.document,args.proxies)
        else:
            #print(Batch_scan(args.many))
            Many_Batch=Batch_scan(args.many) # 批量扫描
            for url in Many_Batch:
                count = 1  # 记录请求多少次
                schedule =1 # 重置字典的数量
                pl += 1  # 记录批量扫描的数量
                print(choose_color_2(
                                     f"扫描结果会保存到result/ProbeBackup/文件夹里面\n正在扫描：{url} 第{str(pl)}个目标"+
                                     f"\n线程数是：{str(args.thread)}"))
                fix(url,args.thread,args.document,args.proxies)


def GUI(url,many,thread,document,proxies,result):
    global GUT_output # 输出到GUI
    global GUT_Sure # 判断是否用到GUI
    global pl
    global count

    GUT_output=result # 输出到GUI

    GUT_Sure=1  # 判断是否用到GUI

    # url=url #URL
    # many='' #  文件名  多个目标保存到一个文件里面进行批量扫描
    # thread = 1 # 线程数
    # document = None # 字典文件
    # proxies = None #代理
    #fix(url, thread, document, proxies)
    #fix(url, thread, document, proxies)


    if url !='' or many != '':
        if thread=='':
            thread=1
        # 设置代理
        if proxies != '':
             acting=proxies
             proxies= {
                "http": "http://" +acting ,
                "https": "http://" + acting}

        # 是否批量扫描
        if many == '': # 不批量扫描

            result.insert(ttk.END,"扫描结果会保存到：result/ProbeBackup/文件夹里面\n你输入的目标地址是: " +
                                 url +
                                 '\n线程数是：' +
                                 str(thread) +
                                 f'\n{"—" * 30}\n')

            fix(url,thread,document,proxies)
        else:

            #result.insert(ttk.END,Batch_scan(many)+"\n")
            Many_Batch=Batch_scan(many) # 批量扫描
            for url in Many_Batch:
                count = 1  # 记录请求多少次
                schedule =1 # 重置字典的数量
                pl += 1  # 记录批量扫描的数量
                result.insert(ttk.END,
                                     f"扫描结果会保存到result/ProbeBackup/文件夹里面\n正在扫描：{url} 第{str(pl)}个目标"+
                                     f"\n线程数是：{str(thread)}\n")
                fix(url,thread,document,proxies)

#GUI("www.baidu.com",'','','','','')