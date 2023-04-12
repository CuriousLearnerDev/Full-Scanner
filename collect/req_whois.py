#import urllib.request
import whois
import requests
from lxml import etree
import  re
import ttkbootstrap as ttk
# choose_color_2  随机颜色

from conf import config
from lib.choose import UseStyle


GUT_output=0 # 输出到GUI
GUT_Sure=0 # 判断是否用到GUI

# 提取出来的结果保存起来
def Searchresults(results_IP):
    Searchresults_document = open(config.Savelocation['whois'], 'a', encoding='utf-8')  # 打开文件写的方式
    Searchresults_document.write((results_IP+'\n'))  # 写入
    Searchresults_document.close()  # 关闭文件

def Whois_centralops(dns):
    data = {
        "__VIEWSTATE": "",
        "addr": dns,
        "dom_whois": "true",
        "net_whois": "true",
        # "net_whois":"true",
    }
    headers = {
        'Host': 'centralops.net',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://centralops.net/co/DomainDossier.aspx',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://centralops.net',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
    }

    html = requests.post(url="http://centralops.net/co/DomainDossier.aspx", headers=headers, data=data,timeout =3)
    html = etree.HTML(html.text)
    divs = html.xpath(r'//body/pre/text()')  # 语法
    #print(divs[0])
    data = f"""
{"*"*14}centralops引起查询： Whois 记录{"*"*14}
{divs[0]}\n\n
    """
    return data

def Whois_check(DNS):

    #try:
    req_whois = whois.whois(DNS)
    data=f"""
{"*"*14}Python-Whois{"*"*14}
查询的域名是："{DNS}"
注册商："{str(req_whois["registrar"])}"
域名服务器："{str(req_whois["whois_server"])}"
推荐网址："{str(req_whois["referral_url"])}"
更新时间："{str(req_whois["updated_date"])}"
创建时间："{str(req_whois["creation_date"])}"
过期时间："{str(req_whois["expiration_date"])}"
名称服务器："{str(req_whois["name_servers"])}"
电子邮件："{str(req_whois["emails"])}"
status："{str(req_whois["status"])}"
dnssec："{str(req_whois["dnssec"])}"
名称："{str(req_whois["name"])}"
组织："{str(req_whois["org"])}"
城市："{str(req_whois["city"])}"
国家："{str(req_whois["country"])}"\n"""

    if GUT_Sure == 1:  # 输出到GUI
        GUT_output.insert(ttk.END, data)
    try:
        centr_alops = Whois_centralops(DNS)
        if GUT_Sure == 1:  # 输出到GUI
            pass
        else:
            print(UseStyle(centr_alops, fore="yellow"))
    except:
        centr_alops=''
        print("centralops.net网页提取错误！")

    if GUT_Sure == 1:  # 输出到GUI
        GUT_output.insert(ttk.END, centr_alops)
    else:
        pass
        print(UseStyle(data, fore="yellow"))

    Searchresults((("#" * 100) + "\n查询的目标是：" + DNS + centr_alops + data + ("#" * 100)))
    # except:
    #     if GUT_Sure == 1:  # 输出到GUI
    #         GUT_output.insert(ttk.END, "\n请求出错：访问不了，或者重新请求\n")
    #     print("请求出错：访问不了，或者重新请求")

def Interface(args):
    DNS=args.whois
    DNS=DNS.strip()

    # 检查dns前面是不是有http或者有https://，有替换空
    DNS=DNS.replace("http://",'')
    DNS = DNS.replace("https://", '')
    DNS = DNS.replace("/", '')

    print("结果会保存到："+config.Savelocation['whois']+"\n当前查询的目标是："+DNS+f'\n\033[0;33m {"*"*60}\033[0m')

    Whois_check(DNS)


def GUI(DNS,result):
    global GUT_output
    global GUT_Sure
    GUT_output=result # 输出到GUI
    GUT_Sure=1  # 判断是否用到GUI

    DNS = DNS.strip()
    # 检查dns前面是不是有http或者有https://，有替换空
    DNS=DNS.replace("http://",'')
    DNS = DNS.replace("https://", '')
    DNS = DNS.replace("/", '')
    GUT_output.insert(ttk.END, "结果会保存到：" + config.Savelocation['whois'] + "\n当前查询的目标是：" + DNS + f'\n{"*" * 60}\n启动查询请稍候！\n')
    GUT_output.insert(ttk.END,'')
    Whois_check(DNS)
    GUT_output.insert(ttk.END, f'完毕！')
# Whois_centralops('zssnp.top')